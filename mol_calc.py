# usr inputs what they want and what they know in order to find mass, moles,
# or anything else. Hopes this helps :)

# constants

av_num = 6.02 * 10**23

print("Please enter everything exactly as you see it. Remember, use 'e+#' to indicate power to. Ex. 10^23 = e+23.")

prob_type = input("What are you trying to find? (mol amount, mass, things...)")

if prob_type == "things":
    thng_init = input("What do you know? (grams, mol amount)")
    if thng_init == "grams":
        thng_init_grams = float(input("Enter mass."))
        thng_init_molarmass = float(input("Enter element or molecules molar mass."))
        print((thng_init_grams * av_num) / thng_init_molarmass)


    if thng_init == "mol amount":
        thng_init_mol = float(input("Enter mol amount."))
        print(thng_init_mol * av_num)


if prob_type == "mass":
    mass_init = input("What do you know? (things, mol amount)")
    if mass_init == "things":
        mass_init_thng = float(input("Enter number of things."))
        mass_init_molarmass = float(input("Enter molar mass."))
        print((mass_init_thng * mass_init_molarmass) / av_num)

    if mass_init == "mol amount":
        mass_init_mol = float(input("Enter mol amount."))
        mass_init_molarmass_molamnt = float(input("Enter molar mass."))
        print(mass_init_mol * mass_init_molarmass_molamnt)



if prob_type == "mol amount":
    mol_init = input("What do you know? (mass, things)")
    if mol_init == "mass":
        mol_init_mass = float(input("Enter the mass."))
        mol_init_molarmass = float(input("Enter molar mass."))
        print(mol_init_mass / mol_init_molarmass)

    if mol_init == "things":
        mol_init_thng = float(input("Enter the number of things."))
        print(mol_init_thng / av_num)
