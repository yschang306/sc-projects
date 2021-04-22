"""
File: weather_master.py
Name: Amber Chang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program computes the highest, lowest, average temperature,
	and the number of cold days as user inputs temperatures
	"""
	print('stanCode "Weather Master 4.0"!')
	temperature = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	if temperature == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = temperature
		minimum = temperature
		total = temperature
		# The sum of temperatures
		n = 1
		# Times of entering the temperature
		if temperature < 16:
			cold_day = 1
		else:
			cold_day = 0
		while True:
			temperature = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
			if temperature == EXIT:
				break
			if temperature > maximum:
				maximum = temperature
			if temperature < minimum:
				minimum = temperature
			if temperature < 16:
				cold_day += 1
			total = total + temperature
			n += 1
		average = total / n
		print('Highest temperature = '+str(maximum))
		print('Lowest temperature = '+str(minimum))
		print('Average = '+str(average))
		print(str(cold_day)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
