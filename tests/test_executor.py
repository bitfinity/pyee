# -*- coding: utf-8 -*-

import pytest

from mock import Mock
from time import sleep

from pyee import ExecutorEventEmitter


class PyeeTestError(Exception):
    pass


def test_executor_emit():
    """Test that ExecutorEventEmitters can emit events.
    """
    ee = ExecutorEventEmitter()

    should_call = Mock()

    @ee.on('event')
    def event_handler():
        should_call(True)

    ee.emit('event')
    sleep(1)

    should_call.assert_called_once()


def test_executor_once():
    """Test that ExecutorEventEmitters also emit events for once.
    """
    ee = ExecutorEventEmitter()

    should_call = Mock()

    @ee.once('event')
    def event_handler():
        should_call(True)

    ee.emit('event')
    sleep(1)

    should_call.assert_called_once()


def test_executor_error():
    """Test that ExecutorEventEmitters handle errors.
    """
    ee = ExecutorEventEmitter()

    should_call = Mock()

    @ee.on('event')
    def event_handler():
        raise PyeeTestError()

    @ee.on('error')
    def handle_error(e):
        should_call(e)

    ee.emit('event')

    sleep(1)

    should_call.assert_called_once()
