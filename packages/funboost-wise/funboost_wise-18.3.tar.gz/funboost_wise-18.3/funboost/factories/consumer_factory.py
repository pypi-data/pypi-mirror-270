# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2022/8/8 0008 13:19
import copy
# from collections import Callable
from typing import Callable

from funboost.consumers.rabbitmq_amqpstorm_consumer import RabbitmqConsumerAmqpStorm

broker_kind__consumer_type_map = {
    0: RabbitmqConsumerAmqpStorm,
}


def get_consumer(*args, broker_kind: int = None, **kwargs):
    """
    :param args: 入参是AbstractConsumer的入参
    :param broker_kind:
    :param kwargs:
    :return:
    """

    if broker_kind not in broker_kind__consumer_type_map:
        raise ValueError(f'设置的中间件种类数字不正确,你设置的值是 {broker_kind} ')
    return broker_kind__consumer_type_map[broker_kind](*args, **kwargs)
