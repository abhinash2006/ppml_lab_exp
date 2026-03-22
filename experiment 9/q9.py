def employee(**details):
    for k,v in details.items():
        print(k,":",v)
employee(name="kiran",id=101,dept="it")