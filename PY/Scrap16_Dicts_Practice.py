
dict1 = {

    "group1" : {
        "a": 20,
        "b": 30,
        "c": 40,
        "d": 10
    },
    "group2" : {
        "a" : 20,
        "b" : {
            "Base": 10,
            "Call": 15,
            "User": 20,
            "Profiles": {

                "acc1": "Colleen",
                "acc2": "Matt",
                "acc3": {

                    "name": "Dummy",
                    "Items": {
                        "Sword",
                        "Shield",
                        "Health Potion"
                    }



                }

            }

        }

   } 

}



cop = dict1.get("group2", {})  .get("b", {})  .get("Profiles")


for user, info in cop.items():
    print(user + ":", info)







