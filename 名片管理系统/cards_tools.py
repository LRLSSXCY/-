# 记录所有的名片字典
card_list = []

def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用 名片管理系统")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)

def new_card():
    print("-" * 50)
    print("新增名片")
    name_input = input("请输入姓名:")
    phone_input = input("请输入电话号码:")
    qq_input = input("请输入QQ号码:")
    email_input = input("请输入邮箱:")

    card_dict = {"name": name_input,
                 "phone": phone_input,
                 "qq": qq_input,
                 "email": email_input}

    card_list.append(card_dict)
    print(card_list)
    print("添加%s的名片成功!" % name_input)

def show_all():
    print("-" * 50)
    print("显示所有名片")

    if len(card_list)== 0:
        print("当前没有任何记录，请使用新增功能添加新名片！")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")
    print("=" * 50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s"
                        %(card_dict["name"],
                          card_dict["phone"],
                          card_dict["qq"],
                          card_dict["email"]))

def search_card():
    print("-" * 50)
    print("查询名片")

    find_name = input("请输入要搜索的姓名：")

    for card_dict in card_list:
        if card_dict["name"]== find_name:
            print("姓名\t\t","电话\t\t","QQ\t\t","邮箱\t\t")
            print("%s\t\t%s\t\t%s\t\t%s"
                  % (card_dict["name"],
                     card_dict["phone"],
                     card_dict["qq"],
                     card_dict["email"]))
            print("=" * 50)
        deal_card(card_dict)
        break

    else:
        print("很抱歉，没有找到 %s" % find_name)

def deal_card(find_dict):
    print(find_dict)
    action_str = input("请选择要执行的操作："
                       "[1]修改[2]删除[0]返回")

    if action_str == "1" :
        print("无需修改的项可以直接回车跳过")
        find_dict["name"] =input_card_info(find_dict["name"],"姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"],"电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"],"QQ：")
        find_dict["email"] = input_card_info(find_dict["email"],"邮箱：")

        print("修改名片成功！")
    elif action_str =="2" :
        card_list.remove(find_dict)
        print("删除名片成功！")

def input_card_info(dict_value, tip_message):
    # 查询中的修改功能的输入完善
    # 提示用户输入内容，若输入了内容，直接返回结果。若没有输入内容，则返回原有值。
    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str
    else :
        return dict_value