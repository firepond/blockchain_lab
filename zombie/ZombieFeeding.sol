import "./ZombieFactory.sol";

pragma solidity ^0.4.19;

contract ZombieFeeding is ZombieFactory {
    
    
    function feedAndMultiply(uint _zombieID, uint _targetDna) internal {
        //取得_targetDna的后dnaModulus位 生成新的僵尸DNA：
        //计算捕食僵尸与被吃人类DNA的平均值 为僵尸添加标识：将新的僵尸DNA最后两位改为“99”。 
        //调用_createZombie生成新僵尸，新僵尸名字为“No-one”。（需要修改_createZombie 函数属性使对继承可见)
        Zombie storage myZombie = zombies[_zombieID];
        require(zombieToOwner[_zombieID] == msg.sender);
        require((now >= myZombie.readyTime));
        uint modDna = _targetDna % dnaModulus;
        uint newDna = (modDna + myZombie.dna) / 200 * 100 + 99;
        _createZombie("No-one", newDna);
        myZombie.readyTime = uint32(now) + coolDownTime;
    }
    
    function _catchAHuman(uint _name) internal pure returns (uint) { 
        uint rand = uint(keccak256(_name)); 
        return rand;
    }
    
    function feedOnHuman(uint _zombieID, uint _humanID) public {
        uint hDna = _catchAHuman(_humanID);
        feedAndMultiply(_zombieID, hDna);
        
    }
}