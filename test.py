def remove_the_mean_person(queue: list):
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """

    queue.sort()
    return queue


print(remove_the_mean_person(['Steve', 'Ultron', 'Natasha', 'Rocket']))