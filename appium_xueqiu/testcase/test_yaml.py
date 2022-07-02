import yaml
def test_yaml_load():
    with open("../page/main.yaml", encoding="utf-8") as f:
        steps = yaml.safe_load(f)
        print(steps)
    for step in steps:
        if "by" in step.keys():
            print("search elements")
        if "action" in step.keys():
            print("multiple action analysis")
            action = step["action"]
            if "click" == action:
                print("click operation")
            if "send" == action:
                value = step["value"]
                print(f"send({value})")

def test_replace():
    _parame = {"name": "12345"}
    str = "xxxxxxxxxxxx ${name} lllllll${name}llllllllll"
    for key, value in _parame.items():
        #str = str.replace(f'${{{key}}}', value)
        str = str.replace('${'+key+'}', value)
    print(str)


