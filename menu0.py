def menu0():
    print("Command:\n 1. Overviewand Key Aspects Screening \n 2. Entry for Key Parameters \n 3. Historical Returns on Graph  \n 4. Scoring Model \n 5. Back to Menu0")

    menu_option = int(input("Please select an option: "))

    if menu_option == 1:
        import Overview_Screener 
    elif menu_option == 2:
        import Parameters_Entries
    elif menu_option == 3:
        import Plot_Graph
    elif menu_option == 4:
        import Score_Model 
    # menu not proceed if option 6 entered twice
    elif menu_option == 5:
        menu0()


menu0()
