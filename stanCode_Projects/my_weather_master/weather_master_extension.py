"""
File: weather_master_extension.py
Name: Amber Chang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days(below 16 degrees),
and hot days(30 degrees or above) among the inputs.
"""

# These constants control when to stop
EXIT = -100
END = 100


def main():
	"""
	This program computes the highest, lowest, average temperature,
	and the number of cold days and hot days as user inputs temperatures.
	Also, it provides reminders based on the cold and hot days.
	"""
	while True:
		print('')
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
			if temperature >= 30:
				hot_day = 1
			else:
				hot_day = 0
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
				if temperature >= 30:
					hot_day += 1
				total = total + temperature
				n += 1
			average = total / n
			print('Highest temperature = '+str(maximum))
			print('Lowest temperature = '+str(minimum))
			print('Average = '+str(average))
			print(str(cold_day)+' cold day(s)', end="")
			if cold_day > 0:
				print(': Remember to put on gloves and scarf!')
			else:
				print('')
			print(str(hot_day)+' hot day(s)', end="")
			if hot_day > 0:
				print(': Make sure you drink enough water!')
			else:
				print('')
			if cold_day == 0 and hot_day == 0:
				print('The overall weather is comfortable!')
		print('')
		restart = int(input('Enter any number other than '+str(END)+' to start a new program (or '+str(END)+' to end).'))
		if restart == END:
			break


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
