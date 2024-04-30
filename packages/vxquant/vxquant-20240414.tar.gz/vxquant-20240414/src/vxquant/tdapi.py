"""tdapi"""

import polars as pl
from typing import Any, Dict, Optional, Union, List
from multiprocessing import Lock
from vxutils import VXContext
from vxutils.provider import AbstractProvider, AbstractProviderCollection
from vxquant.models.base import VXTick
from vxquant.models.base import VXOrder, VXCashInfo, VXPosition, VXExecRpt
from vxquant.models.preset import VXMarketPreset
from vxquant.models.nomalize import to_symbol

__all__ = [
    "VXTdAPI",
    "VXOrderBatchProvider",
    "VXGetAccountProvider",
    "VXGetOrderProvider",
    "VXGetPositionProvider",
    "VXGetExecRptProvider",
]


class VXTdAPI(AbstractProviderCollection):
    __defaults__ = {
        "current": {
            "mod_path": "vxquant.mdapi.VXHQProvider",
            "params": {},
        },
        "order_batch": {"mod_path": "vxquant.tdapi.VXOrderBatchProvider", "params": {}},
        "get_positions": {
            "mod_path": "vxquant.tdapi.VXGetPositionProvider",
            "params": {},
        },
        "get_orders": {"mod_path": "vxquant.tdapi.VXGetOrderProvider", "params": {}},
        "get_execrpts": {
            "mod_path": "vxquant.tdapi.VXGetExecRptProvider",
            "params": {},
        },
        "get_account": {
            "mod_path": "vxquant.tdapi.VXGetAccountProvider",
            "params": {},
        },
    }

    def order_volume(
        self,
        symbol: str,
        volume: int,
        price: Optional[float] = None,
        account_id: Optional[str] = None,
    ) -> VXOrder:
        """下单函数

        Arguments:
            symbol {str} -- 证券代码
            volume {int} -- 下单数量，正数为买，负数为卖
            price {Optional[float]} -- 委托价格 (default: {None})

        Returns:
            VXOrder -- 返回下单订单信息
        """
        symbol = to_symbol(symbol)
        order_side = "Buy" if volume > 0 else "Sell"
        order_type = (
            "Market"
            if price is None
            and VXMarketPreset(symbol=symbol).security_type.name == "BOND_CONVERTIBLE"
            else "Limit"
        )
        if price is None:
            ticks = self.current(symbol).filter(pl.col("symbol") == symbol)
            price = ticks["ask1"][0] if order_side == "Buy" else ticks["bid1"][0]

        order = VXOrder(
            account_id=account_id or "default",
            symbol=symbol,
            volume=abs(volume),
            price=price,
            order_side=order_side,
            order_type=order_type,
        )
        return self.order_batch([order], df=False).values()[0]


class VXHQCallBackProvider(AbstractProvider):
    """行情回调接口"""

    def start_up(self, context: VXContext) -> None:
        """启动函数"""
        super().start_up(context)

        data: Dict[str, List[Any]] = {col: [] for col in VXTick.model_fields.keys()}
        self._ticks = pl.DataFrame(data)
        self._lock = Lock()

    def __call__(self, *symbols: List[str]) -> pl.DataFrame:
        """行情回调函数"""
        if len(symbols) == 1 and isinstance(symbols[0], list):
            symbols = symbols[0]

        with self._lock:
            return self._ticks.filter(pl.col("symbol").is_in(symbols))

    def on_tick(self, ticks: pl.DataFrame) -> None:
        """行情回调函数"""
        if ticks.shape[0] == 0:
            return

        with self._lock:
            self._ticks = pl.concat(
                [
                    self._ticks.filter(pl.col("symbol").is_in(ticks["symbol"]).not_()),
                    ticks,
                ]
            )


class VXOrderBatchProvider(AbstractProvider):
    """批量下单接口"""

    def __call__(
        self, orders: List[VXOrder], *, df: bool = False
    ) -> Union[Dict[str, VXOrder], pl.DataFrame]:
        """下单函数

        Arguments:
            orders {List[VXOrder]} -- 订单列表
            df {bool} -- 是否返回DataFrame (default: {False})

        Returns:
            Union[VXOrder, pl.DataFrame]  -- 委托订单信息
        """
        ret_orders = self._place_order(orders)
        return (
            pl.DataFrame([order.model_dump() for order in ret_orders.values()])
            if df
            else ret_orders
        )

    def _place_order(self, orders: List[VXOrder]) -> Dict[str, VXOrder]:
        """实际下单函数"""
        raise NotImplementedError


class VXOrderCancelProvider(AbstractProvider):
    def __call__(self, order_id: str) -> VXOrder:
        """撤单函数

        Arguments:
            order_id {str} -- 订单ID

        Returns:
            VXOrder -- 返回撤单订单信息
        """
        raise NotImplementedError


class VXGetAccountProvider(AbstractProvider):
    """获取账户信息接口"""

    def __call__(self, account_id: str = "default") -> VXCashInfo:
        """获取账户信息

        Keyword Arguments:
            account_id {str} -- 账户ID (default: {"default"})

        Returns:
            Any -- 账户信息
        """
        raise NotImplementedError


class VXGetOrderProvider(AbstractProvider):
    """获取订单信息接口"""

    def __call__(
        self,
        order_id: str = "",
        *,
        account_id: str = "default",
        is_finished: bool = False,
        df: bool = False,
    ) -> Union[List[VXOrder], pl.DataFrame]:
        """获取订单信息

        Keyword Arguments:
            order_id: str -- 订单ID (default: {""})
            account_id {str} -- 账户ID (default: {"default"})
            is_finished {bool} -- 是否已完成 (default: {False})
            df {bool} -- 是否返回dataframe格式 (default: {False})

        Returns:
            Union[List[VXOrder],pl.DataFrame] -- 订单信息
        """
        raise NotImplementedError


class VXGetPositionProvider(AbstractProvider):
    """获取持仓信息接口"""

    def __call__(
        self, account_id: str = "default", account_type: str = "STOCK", df: bool = False
    ) -> Union[Dict[str, VXPosition], pl.DataFrame]:
        """获取持仓信息

        Keyword Arguments:
            account_id {str} -- 账户ID (default: {"default"})

        Returns:
            Union[List[VXPosition],pl.DataFrame] -- 持仓信息
        """
        raise NotImplementedError


class VXGetExecRptProvider(AbstractProvider):
    """获取成交信息接口"""

    def __call__(
        self, execrpt_id: str = "", *, account_id: str = "default", df: bool = False
    ) -> Union[List[VXExecRpt], pl.DataFrame]:
        """获取成交信息

        Keyword Arguments:
            execrpt_id {str} -- 成交信息订单号 (default: {""})
            account_id {str} -- 账户id (default: {"default"})
            df {bool} -- 是否返回dataframe格式 (default: {False})

        Returns:
            Union[List[VXExecRpt], pl.DataFrame] -- 成交信息
        """
        raise NotImplementedError


if __name__ == "__main__":
    tdapi = VXTdAPI()
