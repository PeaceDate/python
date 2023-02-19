# Strings
if __name__ == '__main__':
    name = "Andrii"
    job = "QA Engineer"
    email = "test@test.com"

    who_am_i_1 = "My name is" + " " + name + ", write me on" + " " + email + " " + "and I'm a" + " " + job
    who_am_i_2 = "My name is {}, write me on {} and I'm a {}".format(name, email, job)
    who_am_i_3 = "My name is %s, write me on %s and I'm a %s" % (name, email, job)
    who_am_i_4 = f"My name is {name}, write me on {email} and I'm a {job}"

    print(who_am_i_1)
    print(who_am_i_2)
    print(who_am_i_3)
    print(who_am_i_4)
