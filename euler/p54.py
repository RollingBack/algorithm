#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 31/05/2017 9:59 AM
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : p54.py
# @Software: PyCharm Community Edition


class Poker(object):
    __slots__ = "points", "suit"

    def __init__(self, points, suit):
        if not points.isdigit():
            try:
                points = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[points]
            except KeyError as e:
                raise Exception('不存在的点数')
        else:
            points = int(points)
            if points < 1 or points > 13:
                raise Exception('不存在的点数')
        self.points = points
        if suit not in ['C', 'D', 'S', 'H']:
            raise Exception('不存在的花色')
        self.suit = suit

    def __lt__(self, other):
        return self.points < other.points

    def __eq__(self, other):
        return self.points == other.points

    def __cmp__(self, other):
        if self.points < other.points:
            return -1
        elif self.points > other.points:
            return 1
        else:
            return 0

    def __str__(self):
        if self.points > 9:
            code = {10: "Ten", 11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}[self.points]
        else:
            code = str(self.points)
        suit = {'S': '♠', 'H': '♥', 'D': '♦', 'C': '♣'}[self.suit]
        return '{0}{1}'.format(code, suit)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        # rate = {'S': 1, 'H': 2, 'D': 3, 'C': 4}
        # return rate[self.suit]*self.points
        return self.points


class Hand(object):
    def __init__(self, hand):
        self.pokers = []
        for each in hand:
            each = list(each)
            self.pokers.append(Poker(*each))
        self.pokers.sort()

    def __str__(self):
        return str(self.pokers)

    def __iter__(self):
        return self.pokers.__iter__()

    def __len__(self):
        return len(self.pokers)

    @property
    def weight(self):
        if not self.is_flush():
            pairs = self.get_pairs()
            if pairs == 4:
                points = sorted([x.points for x in self.pokers])
                count = points.count(points[0])
                if count == 1 or count == 4:
                    # four of a kind
                    return 8
                else:
                    # full house
                    return 7
            # one pair
            elif pairs == 2:
                return 2
            # two pairs
            elif pairs == 3:
                points = sorted([x.points for x in self.pokers])
                max_count = max([points.count(x) for x in points])
                if max_count ==  3:
                    return 4
                return 3
            # straight
            if self.is_straight():
                return 5
            # high card
            return 1
        # flush
        if not self.is_straight():
            return 6
        if self.pokers[0].points != 10:
            # straight flush
            return 9
        # royal flush
        return 10

    def is_straight(self):
        points = sorted([x.points for x in self.pokers])
        for index in range(len(points)-1):
            if points[index] + 1 != points[index + 1]:
                return False
        return True

    def is_flush(self):
        all_suit = self.pokers[0].suit
        for each in self.pokers:
            if each.suit != all_suit:
                return False
        return True

    def get_pairs(self):
        points = [x.points for x in self.pokers]
        length = len(points)
        return length - len(set(points)) + 1

    def __lt__(self, other):
        return self.__cmp__(other) == -1

    def __eq__(self, other):
        length = len(self.pokers)
        length_others = len(other)
        if length != length_others:
            return False
        other.pokers.sort()
        for i in range(length):
            if self.pokers[i] != other.pokers[i]:
                return False
        return True

    def __cmp__(self, other):
        weight_self = self.weight
        weight_other = other.weight
        if weight_self > weight_other:
            return 1
        elif weight_self < weight_other:
            return -1
        else:
            #high card
            if weight_self == 1:
                return self.compare_two(self.pokers, other.pokers)
            # one pair
            elif weight_self == 2:
                groups_self = self.group_by_count()
                groups_others = other.group_by_count()
                if groups_self[1][0] > groups_others[1][0]:
                    return 1
                elif groups_self[1][0] < groups_others[1][0]:
                    return -1
                else:
                    return self.compare_two(groups_self[0], groups_others[0])
            # two pairs
            elif weight_self == 3:
                groups_self = self.group_by_count()
                groups_others = other.group_by_count()
                r = self.compare_two(groups_self[1], groups_others[1])
                if r != 0:
                    return r
                return self.compare_two(groups_self[0], groups_others[0])
            # three of a kind
            elif weight_self == 4:
                groups_self = self.group_by_count()
                groups_others = other.group_by_count()
                r = self.compare_two(groups_self[2], groups_others[2])
                if r != 0:
                    return r
                return self.compare_two(groups_self[0], groups_others[0])
            # straight
            elif weight_self == 5:
                pokers = sorted(self.pokers)
                other = other.sort()
                return pokers[0].__cmp__(other=other[0])
            # flush
            elif weight_self == 6:
                return self.compare_two(self.pokers, other.pokers)
            # full house
            elif weight_self == 7:
                groups_self = self.group_by_count()
                groups_others = other.group_by_count()
                r = self.compare_two(groups_self[2], groups_others[2])
                if r != 0:
                    return r
                return self.compare_two(groups_self[1], groups_others[1])
            # four of a kind
            elif weight_self == 8:
                groups_self = self.group_by_count()
                groups_others = other.group_by_count()
                r = self.compare_two(groups_self[3], groups_others[3])
                if r != 0:
                    return r
                return self.compare_two(groups_self[0], groups_others[0])
            # straight flush
            elif weight_self == 9:
                pokers = sorted(self.pokers)
                other = other.sort()
                return pokers[0].__cmp__(other=other[0])
            elif weight_self == 10:
                return 0

    def group_by_count(self):
        def count_poker(poker):
            return self.pokers.count(poker)
        final = []
        for times in range(1, 5):
            final.append(list(set(filter(lambda x: count_poker(x) == times, self.pokers))))
        return final

    @staticmethod
    def compare_two(x, y):
        a = sorted(x, reverse=True)
        b = sorted(y, reverse=True)
        for index in range(len(a)):
            if a[index] > b[index]:
                return 1
            elif a[index] < b[index]:
                return -1
            else:
                continue
        return 0

name = {
    1: 'high card',
    2: 'one pair',
    3: 'two pairs',
    4: 'three of a kind',
    5: 'straight',
    6: 'flush',
    7: 'full house',
    8: 'four of a kind',
    9: 'straight flush',
    10: 'royal flush'
}
# print(Hand('5H 5C 6S 7S KD'.split(' ')) > Hand('2C 3S 8S 8D TD'.split(' ')))
# print(Hand('5D 8C 9S JS AC'.split(' ')) > Hand('2C 5C 7D 8S QH'.split(' ')))
# print(Hand('2D 9C AS AH AC'.split(' ')) > Hand('3D 6D 7D TD QD'.split(' ')))
# print(Hand('4D 6S 9H QH QC'.split(' ')) > Hand('3D 6D 7H QD QS'.split(' ')))
# print(Hand('2H 2D 4C 4D 4S'.split(' ')) > Hand('3C 3D 3S 9S 9D'.split(' ')))
count_player1_win = 0
count_player2_win = 0
with open('./p054_poker.txt', 'r') as f:
    for each_line in f.readlines():
        each_line = each_line.strip("\n ").split(' ')
        player1_hand = Hand(each_line[:5])
        player2_hand = Hand(each_line[5:])
        # print(player1_hand,' is ', name[player1_hand.weight])
        # print(player2_hand, ' is ', name[player2_hand.weight])
        if player1_hand > player2_hand:
            count_player1_win += 1
        else:
            count_player2_win += 1
    print(count_player1_win)



