//新建一个文件ZombieAttack.sol，在其中新建合约ZombieAttack，继承自ZombieHelper。
//在这之下编辑新的合约的主要部分。 
//最终目的是达到这样一个流程：
//你选择一个自己的僵尸，然后选择一个对手的僵尸去攻击。 
//如果你是攻击方，你将有70%的几率获胜，防守方将有30%的几率获胜。 
//所有的僵尸（攻守双方）都将有一个 winCount 和一个 lossCount，这两个值都将根据战斗结果增长。
//若攻击方获胜，这个僵尸将升级并产生一个新僵尸。 
//如果攻击方失败，除了失败次数将加一外，什么都不会发生。 
//无论输赢，当前僵尸的冷却时间都将被激活。
import "./ZombieHelper.sol";

pragma solidity ^0.4.19;

contract ZombieAttack is ZombieHelper {
    function attackZombie(uint _invaderZombieID, uint _targetZombieID) public returns(int) {
        require(msg.sender == zombieToOwner[_invaderZombieID]);
        Zombie storage invader = zombies[_invaderZombieID];
        Zombie storage defender = zombies[_targetZombieID];
        // 生成一个0到100的随机数: 
        uint randNonce = 0; 
        int invaderRandom = int(uint(keccak256(now, msg.sender, randNonce, _targetZombieID)) % 100); 
        randNonce++; 
        int defenderRandom = int(uint(keccak256(now, msg.sender, randNonce, _invaderZombieID)) % 100);
        int dice = invaderRandom - defenderRandom;
        if(dice > -40) {
            invader.winCount++;
            defender.lossCount++;
            //spoil of war
            invader.level++;
            _createZombie("spoil_of_war", uint(keccak256(now, msg.sender, randNonce)));
        } else {
            invader.lossCount++;
            defender.winCount++;
        }
        invader.readyTime = uint32(now) + coolDownTime;
        return dice;
    }
    
}