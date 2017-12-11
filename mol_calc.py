# usr inputs what they want and what they know in order to find mass, moles,
# or anything else. Hopes this helps :)

# constants

av_num = 6.02 * 10**23

print "Please enter everything exactly as you see it. Remember, use '**' to indicate power-to, ex 10^23 = 10**23." \

prob_type = raw_input("What are you trying to find? (mol amount, mass, things...)")

if prob_type == "things":
    thng_init = raw_input("What do you know? (grams, mol amount)")
    if thng_init == "grams":
        thng_init_grams = input("Enter mass.")
        thng_init_molarmass = input("Enter element or molecules molar mass.")
        mol_and_mass = thng_init_grams * av_num
        final_thng_grams = mol_and_mass / thng_init_molarmass
        print final_thng_grams


    if thng_init == "mol amount":
        thng_init_mol = input("Enter mol amount.")
        mol_and_molarmass = thng_init_mol * av_num
        print mol_and_molarmass


if prob_type == "mass":
    mass_init = raw_input("What do you know? (things, mol amount)")
    if mass_init == "things":
        mass_init_thng = input("Enter number of things.")
        mass_init_molarmass = input("Enter molar mass.")
        thng_molarmass = mass_init_thng * mass_init_molarmass
        final_mass_thng = thng_molarmass / av_num
        print final_mass_thng

    if mass_init == "mol amount":
        mass_init_mol = input("Enter mol amount.")
        mass_init_molarmass_molamnt = input("Enter molar mass.")
        final_mass_mol = mass_init_mol * mass_init_molarmass_molamnt
        print final_mass_mol



if prob_type == "mol amount":
    mol_init = raw_input("What do you know? (mass, things)")
    if mol_init == "mass":
        mol_init_mass = input("Enter the mass.")
        mol_init_molarmass = input("Enter molar mass.")
        final_mol_mass = mol_and_mass / mol_and_molarmass
        print final_mol_mass

    if mol_init == "things":
        mol_init_thng = input("Enter the number of things.")
        final_mol_thng = mol_init_thng / av_num
        print final_mol_thng
