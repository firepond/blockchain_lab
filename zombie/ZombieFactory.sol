import "./Ownable.sol";

pragma solidity ^0.4.19;

contract ZombieFactory is Ownable { 
    
    uint dnaDigits = 16;
    uint dnaModulus = 10 ** 16;
    
    uint32 coolDownTime = 1 minutes;
    
    Zombie[] public zombies;
    
    struct Zombie {
        uint32 winCount;
        uint32 lossCount;
        uint32 level;
        uint32 readyTime;
        string name;
        uint dna;
    } 
    
    mapping (uint => address) public zombieToOwner;
    mapping (address => uint) ownerZombieCount;
    
    function createRandomZombie(string _name) public {
        require(ownerZombieCount[msg.sender]==0);
        uint randDna = _generateRandomDna(_name);
        _createZombie(_name, randDna);
        
    }
    
    function _createZombie(string _name, uint _dna) internal {
        uint zombieId = zombies.push(Zombie(0, 0, 0, uint32(now), _name, _dna)) - 1;
        zombieToOwner[zombieId] = msg.sender;
        ownerZombieCount[zombieToOwner[zombieId]]++;
        NewZombie(zombieId, _name, _dna);
    } 
    
    function _generateRandomDna(string _str) private view returns (uint) {
        bytes32 hash = keccak256(_str);
        uint h = uint(hash);
        uint result = h % dnaModulus;
        return result;
    }
    
    
    
    event NewZombie(uint zombieId, string name, uint dna);
    
    
}