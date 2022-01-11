from brownie import network
import pytest
import time
from scripts.deploy_lottery import deploy_lottery
from scripts.helpful_scripts import (
    LOCAL_BLCOKCHAIN_ENVIRONMENTS,
    fund_with_link,
    get_account,
)
from scripts.deploy_lottery import deploy_lottery


def test_can_pick_winner():
    # arrange
    if network.show_active() in LOCAL_BLCOKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee() + 10000000})
    lottery.enter({"from": account, "value": lottery.getEntranceFee() + 10000000})
    fund_with_link(lottery)
    lottery.endLottery({"from": account})
    time.sleep(60)
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
