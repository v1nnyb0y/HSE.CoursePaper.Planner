from data.tmp.data import task_list


if __name__ == "__main__":
    for d in task_list:
        d.add_to_notion()
