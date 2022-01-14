// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 */
contract Demo {

    string data = "test data";

    /**
     * @dev Store value in variable
     * @param val value to store
     */
    function store(string memory val) public {
        data = val;
    }


    /**
     * @dev Return value 
     * @return value of 'number'
     */
    function retrieve() public view returns (string memory){
        return data;
    }
}