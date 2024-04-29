import json
from multiprocessing import cpu_count, Pool
from random import random, choice
from typing import List, Tuple, Dict, Union

import numpy as np
import relic_engine
import itertools

class SimulationEngine:
    """
    A class for simulating Warframe relic runs and calculating rewards.
    """

    def __init__(self):
        # Represents the number of "runs" required to complete one "cycle" of a relic run style
        self.num_runs_dict = {
            'Solo': 1,
            '1b1': 4,
            '2b2': 2,
            '3b3': (4 / 3),
            '4b4': 1,
            '8b8': 1,
        }
        self.__rarity_dict = {
            'i': {
                ((25 + (1 / 3)) / 100): "Common",
                .11: "Uncommon",
                .02: "Rare"
            },
            'e': {
                ((23 + (1 / 3)) / 100): "Common",
                .13: "Uncommon",
                .04: "Rare"
            },
            'f': {
                .2: "Common",
                .17: "Uncommon",
                .06: "Rare"
            },
            'r': {
                (1 / 6): "Common",
                .2: "Uncommon",
                .1: "Rare"
            },
        }
        self._drop_data_cache = {}

    def get_set_price(self, prime_part: str) -> float:
        """
        Get the price of a prime part set.

        Args:
            prime_part (str): The name of the prime part.

        Returns:
            float: The price of the prime part set.
        """
        set_name = relic_engine.get_set_name(prime_part) + " Set"
        return relic_engine.get_price(set_name)

    def get_drop_priority(self, relics: List[Dict[str, List[str]]], min_price: float = 30) -> Dict[str, int]:
        """
        Get the drop priority of prime parts based on their prices and ducat values.

        Args:
            relics (List[Dict[str, List[str]]]): A list of dictionaries containing relic information.
            min_price (float): The minimum price threshold for platinum priority.

        Returns:
            Dict[str, int]: A dictionary mapping prime parts to their drop priority.
        """
        plat_list = []
        ducat_list = []

        relic_dict = relic_engine.get_relic_dict()

        for relic_info in relics:
            for relic in relic_info['relics']:
                for drop in relic_dict[relic]:
                    if self.get_set_price(drop) >= min_price:
                        plat_list.append([drop, relic_engine.get_price(drop)])
                    else:
                        ducat_list.append([drop, relic_engine.get_ducats(drop)])

        drop_priority = {k: v + 1 for v, k in enumerate([item[0] for item in
                                                         sorted(plat_list, key=lambda x: x[1], reverse=True)])}

        drop_priority.update({k: v + 101 for v, k in enumerate([item[0] for item in
                                                                sorted(ducat_list, key=lambda x: x[1], reverse=True)])})

        return drop_priority

    def get_possible_rewards(self, relics: List[Dict[str, List[str]]]) -> List[Dict[str, Dict[str, Union[float, str]]]]:
        """
        Get the possible rewards for a list of relics with their corresponding refinements.

        Args:
            relics (List[Dict[str, List[str]]]): A list of dictionaries containing relic information.

        Returns:
            List[Dict[str, Dict[str, Union[float, str]]]]: A list of dictionaries representing the possible rewards.
        """
        drops = []
        for relic_info in relics:
            for relic in relic_info['relics']:
                refinement = relic_info['refinement']
                relic_drops = relic_engine.get_relic_drops(relic, refinement)
                drop_dict = {}
                for drop in relic_drops:
                    drop_dict[drop] = {'chance': relic_drops[drop],
                                       'refinement': refinement}
                drops.append(drop_dict)

        return drops

    def get_rarity(self, chance: float, refinement: str) -> str:
        """
        Get the rarity of a drop based on its chance and refinement level.

        Args:
            chance (float): The chance of the drop.
            refinement (str): The refinement level of the relic.

        Returns:
            str: The rarity of the drop.
        """
        return self.__rarity_dict[refinement][chance]

    def get_drop(self, reward_lists: List[Dict[str, Dict[str, Union[float, str]]]]) -> List[str]:
        """
        Get a random drop from a list of reward lists.

        Args:
            reward_lists (List[Dict[str, Dict[str, Union[float, str]]]]): A list of reward lists.

        Returns:
            List[str]: A list containing the selected drop and its rarity.
        """
        reward_list = choice(reward_lists)
        drop_chances, drop_items, drop_rarities = self._prepare_drop_data(reward_list)

        drop_index = np.random.choice(len(drop_chances), p=drop_chances)

        selected_drop = drop_items[drop_index]
        selected_rarity = drop_rarities[drop_index]

        return [selected_drop, selected_rarity]

    def _prepare_drop_data(self, reward_list: Dict[str, Dict[str, Union[float, str]]]) -> Tuple[
        np.ndarray, List[str], List[str]]:
        """
        Prepare the drop data by extracting chances, items, and rarities from the reward list.

        Args:
            reward_list (Dict[str, Dict[str, Union[float, str]]]): The reward list.

        Returns:
            Tuple[np.ndarray, List[str], List[str]]: A tuple containing drop chances, drop items, and drop rarities.
        """
        reward_key = json.dumps(reward_list, sort_keys=True)
        if reward_key in self._drop_data_cache:
            return self._drop_data_cache[reward_key]

        drop_chances = []
        drop_items = []
        drop_rarities = []

        for item, info in reward_list.items():
            chances = info['chance']
            if not isinstance(chances, list):
                chances = [chances]

            for chance in chances:
                drop_chances.append(chance)
                drop_items.append(item)
                drop_rarities.append(self._get_rarity(chance, info['refinement']))

        drop_data = np.array(drop_chances), drop_items, drop_rarities
        self._drop_data_cache[reward_key] = drop_data
        return drop_data

    def _get_rarity(self, chance: float, refinement: str) -> str:
        """
        Get the rarity of a drop based on its chance and refinement level (optimized version).

        Args:
            chance (float): The chance of the drop.
            refinement (str): The refinement level of the relic.

        Returns:
            str: The rarity of the drop.
        """
        rarity_dict = self.__rarity_dict[refinement]
        for threshold, rarity in rarity_dict.items():
            if chance == threshold:
                return rarity

    def get_best_drop(self, drops: List[List[str]], drop_order: Dict[str, int]) -> Tuple[str, List[List[str]]]:
        """
        Get the best drop from a list of drops based on the drop order.

        Args:
            drops (List[List[str]]): A list of drops.
            drop_order (Dict[str, int]): A dictionary representing the drop order.

        Returns:
            Tuple[str, List[List[str]]]: A tuple containing the best drop and the list of drops.
        """
        return sorted(drops, key=lambda val: drop_order[val[0]])[0][0], drops

    def get_reward_screen(self, relics: List[List[Dict[str, Dict[str, Union[float, str]]]]]) -> List[List[str]]:
        """
        Get the reward screen for a list of relics.

        Args:
            relics (List[List[Dict[str, Dict[str, Union[float, str]]]]]): A list of relics.

        Returns:
            List[List[str]]: A list of drops representing the reward screen.
        """
        reward_screen = []
        for relic in relics:
            reward_screen.append(self.get_drop(relic))

        return reward_screen

    def process_run(self, drops: List[Dict[str, Dict[str, Union[float, str]]]],
                    offcycle_drops: List[List[Dict[str, Dict[str, Union[float, str]]]]], style: str,
                    drop_priority: Dict[str, int]) -> Tuple[str, List[List[str]]]:
        """
        Process a single relic run and determine the best drop and reward screen.

        Args:
            drops (List[Dict[str, Dict[str, Union[float, str]]]]): A list of drops.
            offcycle_drops (List[List[Dict[str, Dict[str, Union[float, str]]]]]): A list of offcycle drops.
            style (str): The style of the relic run.
            drop_priority (Dict[str, int]): A dictionary representing the drop priority.

        Returns:
            Tuple[str, List[List[str]]]: A tuple containing the best drop and the reward screen.
        """
        num_drops = self._get_num_drops(style)
        num_offcycle_drops = self._get_num_offcycle_drops(style, offcycle_drops)
        relics = self._generate_relics(drops, offcycle_drops, num_drops, num_offcycle_drops)
        best_drop, reward_screen = self.get_best_drop(self.get_reward_screen(relics), drop_priority)
        return best_drop, reward_screen

    def _get_num_drops(self, style: str) -> int:
        """
        Get the number of drops based on the relic run style.

        Args:
            style (str): The style of the relic run.

        Returns:
            int: The number of drops.
        """
        return 1 if style == 'Solo' else int(style.split('b')[0])

    def _get_num_offcycle_drops(self, style: str,
                                offcycle_drops: List[List[Dict[str, Dict[str, Union[float, str]]]]]) -> List[int]:
        """
        Get the number of offcycle drops based on the relic run style and offcycle drops.

        Args:
            style (str): The style of the relic run.
            offcycle_drops (List[List[Dict[str, Dict[str, Union[float, str]]]]]): A list of offcycle drops.

        Returns:
            List[int]: A list of the number of offcycle drops for each offcycle drop list.
        """
        num_drops = self._get_num_drops(style)
        num_offcycle_lists = len(offcycle_drops)

        if num_offcycle_lists == 0:
            return []

        offcycle_distribution = {
            '1b1': self._distribute_offcycles_1b1,
            '2b2': self._distribute_offcycles_2b2,
            '3b3': self._distribute_offcycles_3b3,
        }

        distribute_func = offcycle_distribution.get(style)

        if distribute_func:
            return distribute_func(num_offcycle_lists)
        else:
            if num_offcycle_lists > 1:
                raise ValueError(f"{style} style cannot have offcycle drops.")
            return [4 - num_drops]

    def _distribute_offcycles_1b1(self, num_offcycle_lists: int) -> List[int]:
        """
        Distribute offcycle drops for the 1b1 style.

        Args:
            num_offcycle_lists (int): The number of offcycle drop lists.

        Returns:
            List[int]: A list of the number of offcycle drops for each offcycle drop list.
        """
        if num_offcycle_lists == 1:
            return [3]
        elif num_offcycle_lists == 2:
            return [2, 1] if random() < 0.5 else [1, 2]
        elif num_offcycle_lists == 3:
            return [1, 1, 1]
        else:
            raise ValueError("1b1 style cannot have more than 3 offcycle lists.")

    def _distribute_offcycles_2b2(self, num_offcycle_lists: int) -> List[int]:
        """
        Distribute offcycle drops for the 2b2 style.

        Args:
            num_offcycle_lists (int): The number of offcycle drop lists.

        Returns:
            List[int]: A list of the number of offcycle drops for each offcycle drop list.
        """
        if num_offcycle_lists == 1:
            return [2]
        elif num_offcycle_lists == 2:
            return [1, 1]
        else:
            raise ValueError("2b2 style cannot have more than 2 offcycle lists.")

    def _distribute_offcycles_3b3(self, num_offcycle_lists: int) -> List[int]:
        """
        Distribute offcycle drops for the 3b3 style.

        Args:
            num_offcycle_lists (int): The number of offcycle drop lists.

        Returns:
            List[int]: A list of the number of offcycle drops for each offcycle drop list.
        """
        if num_offcycle_lists == 1:
            return [1]
        else:
            raise ValueError("3b3 style cannot have more than 1 offcycle list.")
    def _generate_relics(self, drops: List[Dict[str, Dict[str, Union[float, str]]]],
                         offcycle_drops: List[List[Dict[str, Dict[str, Union[float, str]]]]],
                         num_drops: int, num_offcycle_drops: List[int]) -> List[List[Dict[str, Dict[str, Union[float, str]]]]]:
        """
        Generate the relics for the relic run based on drops, offcycle drops, and their respective counts.

        Args:
            drops (List[Dict[str, Dict[str, Union[float, str]]]]): A list of drops.
            offcycle_drops (List[List[Dict[str, Dict[str, Union[float, str]]]]]): A list of offcycle drops.
            num_drops (int): The number of drops.
            num_offcycle_drops (List[int]): The number of offcycle drops for each offcycle drop list.

        Returns:
            List[List[Dict[str, Dict[str, Union[float, str]]]]]: A list of relics for the relic run.
        """
        relics = [drops] * num_drops
        for i, count in enumerate(num_offcycle_drops):
            relics.extend([offcycle_drops[i]] * count)
        return relics

    def simulate_relic(self, relics: List[Dict[str, Union[List[str], str]]], *, style: str = "4b4", amount: int = 1,
                       drop_priority: Dict[str, int] = None) -> Tuple[List[str], List[List[List[str]]]]:
        """
        Simulate a relic run and calculate the rewards.

        Args:
            relics (List[Dict[str, Union[List[str], str]]]): A list of dictionaries containing relic information.
            style (str, optional): The style of the relic run. Defaults to "4b4".
            amount (int, optional): The number of runs to simulate. Defaults to 1.
            drop_priority (Dict[str, int], optional): A dictionary representing the drop priority. Defaults to None.

        Returns:
            Tuple[List[str], List[List[List[str]]]]: A tuple containing the list of reward drops and the list of reward screens.
        """
        drops = self.get_possible_rewards(relics[:1])

        offcycle_drops = []
        if len(relics) > 1:
            offcycle_drops = [self.get_possible_rewards([relic_info]) for relic_info in relics[1:]]

        if drop_priority is None:
            drop_priority = self.get_drop_priority(relics)

        num_runs = self.num_runs_dict.get(style, 1)

        reward_list, reward_screen = self._run_simulations(drops, offcycle_drops, style, drop_priority, amount,
                                                           num_runs)
        return reward_list, reward_screen


    def _run_simulations(self, drops: List[Dict[str, Dict[str, Union[float, str]]]],
                         offcycle_drops: List[List[Dict[str, Dict[str, Union[float, str]]]]],
                         style: str, drop_priority: Dict[str, int], amount: int, num_runs: int) -> Tuple[
        List[str], List[List[List[str]]]]:
        """
        Run the relic simulations and return the reward list and reward screen.

        Args:
            drops (List[Dict[str, Dict[str, Union[float, str]]]]): A list of dictionaries representing the possible rewards.
            offcycle_drops (List[List[Dict[str, Dict[str, Union[float, str]]]]]): A list of lists of dictionaries representing the offcycle rewards.
            style (str): The style of the relic run.
            drop_priority (Dict[str, int]): A dictionary representing the drop priority.
            amount (int): The number of runs to simulate.
            num_runs (int): The number of runs per simulation.

        Returns:
            Tuple[List[str], List[List[List[str]]]]: A tuple containing the list of reward drops and the list of reward screens.
        """
        if amount * num_runs < 50000:
            reward_list, reward_screen = zip(*[self.process_run(drops, offcycle_drops, style, drop_priority)
                                               for _ in itertools.repeat(None, int(amount * num_runs))])
        else:
            num_cores = cpu_count()
            with Pool(num_cores) as pool:
                results = pool.starmap(self.process_run, [(drops, offcycle_drops, style, drop_priority)
                                                          for _ in itertools.repeat(None, int(amount * num_runs))])

            reward_list, reward_screen = zip(*results)
            return list(reward_list), list(reward_screen)
        return list(reward_list), list(reward_screen)
