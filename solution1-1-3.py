lead_singer = 'John'
back_vocal = 'Helen'

# your code goes in here, it should not rely on concrete values of lead_singer and back_vocal:
x, lead_singer = lead_singer, back_vocal
back_vocal = x

# don’t change the code below
print(lead_singer, back_vocal)
