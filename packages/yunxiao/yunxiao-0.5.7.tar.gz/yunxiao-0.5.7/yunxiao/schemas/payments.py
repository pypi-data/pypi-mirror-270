import time

from pydantic import BaseModel, field_validator
from typing import List, Optional
from decimal import Decimal
from datetime import datetime
from .page import Page


class paymentAccountCustoms_Item(BaseModel):
    id: int
    name: str


class Payment(BaseModel):
    orderId: int
    groupId: int
    groupNo: str
    campusId: int
    campusName: str
    studentId: int
    studentName: str
    buyerNameStr: str
    phone: str
    relation: Optional[str]
    orderType: int
    orderStatus: int
    orderTypeDesc: str
    orderStatusDesc: str
    payFact: Decimal
    walletMoney: Decimal
    onlineMoney: Decimal
    offlineMoney: Decimal
    storedCardMoney: Decimal
    storedCardPrincipalMoney: Decimal
    storedCardGiveMoney: Decimal
    payTypeDesc: str
    payTime: datetime
    paymentAccountCustoms: Optional[List[paymentAccountCustoms_Item]]
    payTimeStr: str
    handleTeacherId: int
    handleTeacherName: str
    orderNo: str
    payStatus: Optional[int]
    orderTime: datetime
    sourceType: int
    sourceTypeStr: str
    confirmStatus: int
    confirmOperaId: Optional[int]
    confirmOperaName: Optional[str]
    confirmTime: Optional[datetime]
    btransactionId: Optional[int]

    @field_validator('payTime', 'orderTime', 'confirmTime', mode='before')
    def validate_payTime(cls, v: int):
        return datetime.fromtimestamp(v / 1000) if v else None


class paymentDetailDtos(BaseModel):
    paymentDetailDtos: List[Payment] = []
    totalPayFact: Decimal
    totalWalletMoney: Decimal
    totalOnlineMoney: Decimal
    totalOfflineMoney: Decimal
    totalStoredCardMoney: Decimal
    totalStoredCardPrincipalMoney: Decimal
    totalStoredCardGiveMoney: Decimal


class Payments(BaseModel):
    data: Optional[List[Payment]] = []
    currentTimeMillis: int = 0
    code: int = 200
    msg: str = ""
    page: Page = Page()

    @field_validator('data', mode='before')
    def validate_data(cls, v: dict):
        return paymentDetailDtos(**v).paymentDetailDtos


class PaymentsQueryPayload(BaseModel):
    """
    Attributes:
        payStartTime: str = ""  # 支付时间-起始
        payEndTime: str = ""  # 支付时间-结束
        orderStartTime: str = ""  # 订单创建时间-起始
        orderEndTime: str = ""  # 订单创建时间-结束
        campusIds: List[int] = []  # 校区
        groupNo: str = ""  # 收据编号
        orderNo: str = ""  # 关联订单编号
        handleTeacherId: Optional[int]  # 操作人
        confirmStatusList: List[int] = []  # 入账状态：1-待确认 2-已确认
        revenueType: int = ""  # 收入类型：0-收费 1-转课
        orderStatus: int = ""  # 订单状态：1-已付款 2-已作废
        payType: int = ""  # 支付方式：0-钱包支付 1-线上支付 2-线下收款 3-储值卡支付
        studentIds: List[int] = []  # 学员
        phone: str = ""  # 手机号码
        paymentAccountCustomIds: List[int] = []  # 收款账户
        cardName: str = ""  # 持卡人
        btransactionId: str = ""  # 支付单号
    """
    campusIds: List[int] = []  # 校区
    payStartTime: str = ""  # 支付时间-起始
    payEndTime: str = ""  # 支付时间-结束
    orderStartTime: str = ""  # 订单创建时间-起始
    orderEndTime: str = ""  # 订单创建时间-结束
    btransactionId: str = ""  # 支付单号
    cardName: str = ""  # 持卡人
    confirmStatusList: List[int] = []  # 入账状态：1-待确认 2-已确认
    groupNo: str = ""  # 收据编号
    handleTeacherId: Optional[int] = None
    orderNo: str = ""  # 关联订单编号
    orderStatus: int = None  # 订单状态：1-已付款 2-已作废
    page: Page = Page()
    payType: int = None  # 支付方式：0-钱包支付 1-线上支付 2-线下收款 3-储值卡支付
    paymentAccountCustomIds: List[int] = []  # 收款账户
    phone: str = ""  # 手机号码
    revenueType: int = None  # 收入类型：0-收费 1-转课
    studentIds: List[int] = []  # 学员
    _t_: int = int(time.time() * 1000)
