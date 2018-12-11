import os
import pathlib
import asyncio

import discord
import discord.ext.commands as commands

import enum

class Members(enum.Enum):
    Group   =   0
    Honoka  =   1
    Umi     =   2
    Kotori  =   3
    Maki    =   4
    Hanayo  =   5
    Rin     =   6
    Nozomi  =   7
    Eri     =   8
    Nico    =   9
    #???    =   10

    def get_member(index):
        return Members(index).name
