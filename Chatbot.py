from flask import Flask, request, jsonify
import datetime
import requests
import random

app = Flask(__name__)

# FAQ responses with keyword detection
faq_responses = {
    "github": "My GitHub username is William-Higginbotham, and you can find my portfolio at https://github.com/William-Higginbotham.",
    "portfolio": "You can find my portfolio on GitHub at https://github.com/William-Higginbotham.",
    "contact": "You can contact me via LinkedIn at https://www.linkedin.com/in/william-higginbotham-851556130/ or email me at William.higginbotham1@gmail.com."
}

# List of interesting facts
facts = [
        "Australia is wider than the moon.",
        "Venus is the only planet to spin clockwise.",
        "Allodoxaphobia is the fear of other people’s opinions.",
        "Human teeth are the only part of the body that cannot heal themselves.",
        "Competitive art used to be an Olympic sport.",
        "The first person processed at Ellis Island was a 15-year-old girl from Ireland.",
        "Google Images was created after Jennifer Lopez wore the green dress at the 2000 Grammys.",
        "Lemons float, but limes sink.",
        "The Eiffel Tower was originally made for Barcelona.",
        "It would take 19 minutes to fall to the center of the Earth.",
        "The real name for a hashtag is an octothorpe.",
        "Neil Armstrong’s hair was sold in 2004 for $3,000.",
        "The longest English word is 189,819 letters long.",
        "The tiny pocket in jeans was designed to store pocket watches.",
        "People once ate arsenic to improve their skin.",
        "“The Terminator” script was sold for $1.",
        "Penicillin was first called “mold juice.”",
        "A fear of long words is called Hippopotomonstrosesquippedaliophobia.",
        "The quickest commercial flight in the world is in Scotland.",
        "The first commercial passenger flight lasted only 23 minutes.",
        "No number before 1,000 contains the letter A.",
        "There were active volcanoes on the moon when dinosaurs were alive.",
        "Sudan has more pyramids than any country in the world.",
        "The circulatory system is more than 60,000 miles long.",
        "The Pope can’t be an organ donor.",
        "The world’s longest concert lasted 453 hours.",
        "It’s impossible to hum while holding your nose.",
        "Africa is the only continent in all four hemispheres.",
        "All mammals get goosebumps.",
        "Japan has one vending machine for every 40 people.",
        "McDonald’s once made bubblegum-flavored broccoli.",
        "Finland has more saunas than cars.",
        "The longest time someone has spent holding their breath underwater is 24 minutes and 37 seconds.",
        "Frida Kahlo painted 55 self-portraits.",
        "Avocados are actually fruits, not vegetables.",
        "NFL Super Bowl referees also get Super Bowl rings.",
        "It’s illegal to own only one guinea pig in Switzerland.",
        "Only four countries in the world have national anthems with no lyrics.",
        "The letter “Q” doesn’t appear in any American state’s name.",
        "Walt Disney currently holds the most Academy Awards at a lifetime total of 26.",
        "The average cloud weighs over one million pounds.",
        "Wearing a necktie could reduce blood flow to your brain by up to 7.5 percent.",
        "Animals can also be allergic to humans.",
        "Finland has ranked as the happiest country in the world for 7 years straight.",
        "Bottlenose dolphins are the only other species to have names for themselves.",
        "Your brain alone burns around 400 to 500 calories each day.",
        "Approximately 10% of people are left-handed.",
        "Besides water, tea is the most popular beverage worldwide.",
        "Your heart beats an average of 100,000 times each day.",
        "The first animals to travel to outer space were fruit flies.",
    # Add all remaining facts here
]

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("message", "").lower()

    # Check for FAQ keywords
    for keyword, response in faq_responses.items():
        if keyword in user_input:
            return jsonify({"response": response})

    # Time response
    if "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return jsonify({"response": f"The current time is {current_time}."})

    # Weather response
    elif "weather" in user_input:
        city = request.json.get("city", "")
        api_key = "37104ead748f70ca9eb013e3d2199195"
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

        try:
            response = requests.get(weather_url)
            weather_data = response.json()
            if weather_data["cod"] == 200:
                temperature = weather_data["main"]["temp"]
                description = weather_data["weather"][0]["description"]
                return jsonify({"response": f"The current temperature in {city} is {temperature}°F with {description}."})
            else:
                return jsonify({"response": "Sorry, I couldn't find the weather for that location."})
        except:
            return jsonify({"response": "Error retrieving weather information."})

    # Interesting fact response
    elif "something interesting" in user_input or "tell me something" in user_input:
        fact = random.choice(facts)
        return jsonify({"response": f"Did you know? {fact}"})

    # Default response
    else:
        return jsonify({"response": "I'm sorry, I didn't understand that. If you don't know what to ask, just ask me to tell you something interesting!"})

if __name__ == '__main__':
    app.run(debug=True)
