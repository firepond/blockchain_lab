pragma solidity ^0.5.11;

import "./ZombieFeeding.sol";


contract ZombieHelper is ZombieFeeding {
    uint levelUpFee = 0.001 ether;
    function changeName(uint _zombieID, string _newName) external aboveLevel(2, _zombieID) {
        require(msg.sender == zombieToOwner[_zombieID]);
        zombies[_zombieID].name = _newName;
    }
     function changeDna(uint _zombieID, uint _newDna) external aboveLevel(20, _zombieID) {
        require(msg.sender == zombieToOwner[_zombieID]);
        zombies[_zombieID].dna = _newDna;

    }

    function getZombiesByOwner(address _owner) external view returns(uint[]) {
        uint[] memory result = new uint[](ownerZombieCount[_owner]);
        uint id;
        uint count;
        uint length = zombies.length;
        for (count = id = 0;id < length;id++) {
            if (zombieToOwner[id] == _owner) {
                result[count] = id;
                count++;
            }
        }

        return result;
    }


    function levelUp(uint _zombieId) external payable {
        require(msg.value == levelUpFee);
        zombies[_zombieId].level++;
    }


    function withdraw() external onlyOwner {
        owner.transfer(this.balance);
    }


    function  setLevelUpFee(uint _fee) external onlyOwner{
        levelUpFee = _fee;
    }

    function showLevelUpFeeByFinney() public view returns(uint) {
        return levelUpFee / 1 finney;
    }

    modifier aboveLevel(uint _level, uint _zombieID) {
        if(zombies[_zombieID].level >= _level) {
            _;
        }
    }

}