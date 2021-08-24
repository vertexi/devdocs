#%%
import json

def tack_dict(hazard, switch):
    hazard_title = """<h""" +str(switch) +""">""" + hazard['name'] + """</h""" + str(switch) + """>"""
    print(hazard_title, file=fileptr)
    string_status = 0

    if type(hazard['describe']) == type(dict()):
        tack_dict(hazard['describe'], switch+1)
    if type(hazard['describe']) == type(list()):
        for content in hazard['describe']:
            if type(content) == str:
                if string_status == 0:
                    string_status = 1
                if string_status == 1:
                    print("""<ul>""", file=fileptr)
                    string_status = 2
                content_str = """<li>""" + content.strip() + """</li>"""
                print(content_str, file=fileptr)
            else:
                temp1 = """<h"""+str(switch+1)+""">""" + content['name'] + """</h""" + str(switch+1)+""">"""
                print(temp1, file=fileptr)
                print("""<ul>""", file=fileptr)
                if type(content['describe']) == str:
                        temp2_str = """<li>""" + content['describe'].strip() + """</li>"""
                        print(temp2_str, file=fileptr)
                elif type(content['describe']) == type(list()):
                    for temp3 in content['describe']:
                        temp3_str = """<li>""" + temp3.strip() + """</li>"""
                        print(temp3_str, file=fileptr)
                print("""</ul>""", file=fileptr)
    elif type(hazard['describe']) == str:
        print("""<ul>""", file=fileptr)
        content_str = """<li>""" + hazard['describe'].strip() + """</li>"""
        print(content_str, file=fileptr)
        print("""</ul>""", file=fileptr)
    if string_status == 2:
        print("""</ul>""", file=fileptr)
        string_status = 0
#%%
with open("translated_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#%%
for dicts in data:
    filename = "guidance/"+'guidance'+dicts['code'][6:]+'.html'
    print(filename)
    with open(filename, "w", encoding="utf-8") as fileptr:
        head_title = """<h1>Guide """+dicts['code'][6:]+"""</h1>"""
        print(head_title, file=fileptr)

        class_header = """<p><code>类别：</code>""" + dicts['class']['classname'] + """</p>"""
        print(class_header, file=fileptr)

        if not dicts['class']['classnote'] == list():
            class_note = """<p><code>注：</code>""" + dicts['class']['classnote'] + """</p>"""
            print(class_note, file=fileptr)

        potential_hazards = """<h2>潜在危害</h2>"""
        print(potential_hazards, file=fileptr)
        for hazard in dicts['potential_hazards']:
            hazard_title = """<h3>""" + hazard['name'] + """</h3>"""
            print(hazard_title, file=fileptr)
            print("""<ul>""", file=fileptr)
            if type(hazard['describe']) == type(list()):
                for content in hazard['describe']:
                    content_str = """<li>""" + content.strip() + """</li>"""
                    print(content_str, file=fileptr)
            elif type(hazard['describe']) == str:
                content_str = """<li>""" + hazard['describe'].strip() + """</li>"""
                print(content_str, file=fileptr)
            print("""</ul>""", file=fileptr)

        potential_hazards = """<h2>公共安全</h2>"""
        print(potential_hazards, file=fileptr)
        for hazard in dicts['public_safety']:
            tack_dict(hazard, 3)

        print("""<h2>应急响应</h2>""", file=fileptr)
        for hazard in dicts['emergency_response']:
            tack_dict(hazard, 3)
