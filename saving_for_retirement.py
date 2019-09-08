
def saving_estimate(b_total, a_age, a_saved_per_year):
    a_total = 0 
    while b_total >= a_total:
        a_total += a_saved_per_year
        a_age += 1
    return a_age



def main():
    case = input().split(" ")
    b_age_current = int(case[0])
    b_age_retired = int(case[1])
    b_saved_per_year = int(case[2])
    a_age_current = int(case[3])
    a_saved_per_year = int(case[4])

    num_of_years_saving = b_age_retired - b_age_current
    b_total_saved = num_of_years_saving * b_saved_per_year

    print(saving_estimate(b_total_saved, a_age_current, a_saved_per_year))


if __name__ == "__main__":
    main()