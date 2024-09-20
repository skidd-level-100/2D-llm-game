# this place is for testing weird code

                    percentage = self.resistances[damage_special_type] / 10
                    print(f"percentage:{percentage}")
                    damage_to_take += int(instance[0] - instance[0] * percentage)
                    defense_messsages.append(f"your armour blocked {instance[0] - damage_to_take} of {damage_special_type} damage out of {instance[0]} damage")