import re
import long_responses as long

def message_probability(user_message, recognized_words, single_response = False, required_words = []):
  message_certainty = 0
  has_required_words = True

# for-loop to see if words in the message given by user is 
  for word in user_message:
    if word in recognized_words:
      message_certainty += 1

# calculates the percent of recognized words in a user message, and should return a percent between 0 and 1
  percentage = float(message_certainty) / float(len(recognized_words))

  for word in required_words:
    if word not in user_message:
      has_required_words = False
      break


  if has_required_words or single_response:
    return int(percentage * 100)
  else:
    return 0
  


def check_all_messages(message):

  # a dictionary
  highest_prob_list = {}

  def  response(bot_response, list_of_words, single_response = False, required_words = []):
    nonlocal highest_prob_list
    highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

  # responses ________________________________________________________________________
  response('Hello!', ['hello', 'hi', 'sup', 'hey'], single_response = True)
  response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
  response('See you!', ['bye', 'goodbye', 'adios'], single_response = True)
  

  best_match = max(highest_prob_list, key=highest_prob_list.get)
  print(highest_prob_list)

  return best_match


""" get_response takes in user_input as an input and splits the words up into an array response and returns response"""
def get_response(user_input):
  # This is to split up the message into words, by checking for common punctuation. This also makes sure words are not case sensitive
  split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
  response = check_all_messages(split_message)
  return response


# This tests the response system
while True:
  print('Chatbot: ' + get_response(input('You: ')))