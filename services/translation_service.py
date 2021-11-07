import requests, uuid

# Add your subscription key and endpoint
subscription_key = "75cb7dd61d3043f7b925b930f2b78a37"
endpoint = "https://api.cognitive.microsofttranslator.com"

path = '/translate'
location = 'germanywestcentral'
params = {
    'api-version': '3.0',
    'to': ['en']
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


def translate_text(text):
    body = [{
        'text': text
    }]

    # request = requests.post(constructed_url, params=params, headers=headers, json=body)
    # response = request.json()
    return [{'detectedLanguage': {'language': 'bg', 'score': 1.0},
             'translations': [{
                 'text': "In Epirus and Albania\r\n Main articles: Siege of Ioannina and Siege of Shkodër\r\nAfter Greece's refusal to join the Chattanooga Truce, its troops continued their offensive in Epirus, but were long unsuccessful. The first two storms of the Yanin Fortress (in early December 1912 and 7-9 January 1913) were weaned from the garrison. The third storm (on February 21, 1913) ended with a decisive Greek victory that put out a 26,000-strong Ottoman army. Most of the garrison headed by Esad Pasha is surrendered. After the fall of Ioannina, the Greeks conquered all of Epirus. [130]\r\n\r\nShkodër region (Austro-Hungarian military map from 1904)\r\nThe armistice of 20 November 1912 is also not respected in northern Albania. After the capture of the city of Elbasan, in early December Serbia stopped the offensive of its troops on the Skumbini River with the intention of annexing the territories north of it. The area south of the river remains under the control of the remnants of the Ottoman Vardar Army (Javid Pasha Corps), which withdrew to southern Albania after the defeat at Bitola. In the occupied Albanian lands, a strong ethnic movement against the Serbs developed. In March, Serbian troops crossed the Skumbini in pursuit of Albanian authorities. Although reinforced with several thousand fighters from the Janine garrison, Javid Pasha was crushed and retreated to the city of Berat (March 30). [131]\r\n\r\nThe Montenegrin forces besieging Shkodër were reinforced by Serbian troops, but the two attempts to take control of the fortress (january 25-27 and February 18-19, 1913) failed. [132]\r\n\r\nImmediately after the Armistice on April 1, Serbia withdrew its troops from Albania under the threat of war with Austria-Hungary, which fears that a Serbian outlet on the Adriatic Sea will jeopardize its maritime communications. Montenegrin troops continued the siege of Shkodër and on April 10 entered the fortress abandoned by the Turkish-Albanian garrison, but were soon forced by the Great Powers to leave it. [133] [134]\r\n\r\nIn Eastern Thrace\r\n[Show]\r\nEastern Thrace (1913)\r\nWith the end of London's peace talks, the young Turkish government relied on a partial twist in the war to allow the Ottoman Empire to retain control of Edirne and its region. During the armistice, it trooped up significant troops at the fortified positions near Chatalja (at Istanbul) and Bulair (on the Isthmus of the Galipol Peninsula). The plan of the new Ottoman commander, Ahmed Yset Pasha, to unblock Edirne provides for a triple attack. The main blow must be inflicted on Boulahair by the Gallic Army. It must be assisted by landing on the shore of the Marmara Sea in the back of the Bulgarian defenders. The Croaljan army was tasked with inflicting the second auxiliary strike. [135]\r\n\r\nBulgarian heavy artillery in positions\r\nIn anticipation of the Ottoman counteroffensive, the Bulgarian Command prepared fortified positions for the 1th and 3th Army at Chatalja and along the shores of the Black and Marmara Seas. Under Edirne, the 2nd Army was reinforced with two divisions and siege artillery from Serbia. In mid-December 1912, the Fourth Army was created at the head of General Stylyan Kovachev. Its composition includes the two infantry divisions, which during the first phase of the war acted in Eastern Macedonia and the Rhodope Mountains – the 7th Rila and 2nd Thracian Divisions, as well as the Macedonian-Edirne Militia, the Equestrian Division and the Combined Horse Brigade. [136]\r\n\r\nOn January 26, 1913, Ottoman troops marched from Gallipoli. At the same time, an 8,000-year-old Turkish landing was landed near Sharkoy. In the decisive battle of Bulair, the Gallipole Army was defeated by the 7th Rila Division. Two days later, the Ottoman 10th Corps (Hurshide Pasha) withdrew by sea from the placenta occupied at Sharkoy (Boy at Sharkoy). The Bulgarian Coast Guard repelled several smaller landings in Eastern Thrace. The Ottoman offensive in Chatalja began three days before the offensive in Boulahair (on January 23). [137] After fighting with variable success, in early February the Bulgarian troops withdrew 10-20 km west of Chatalja to the pre-prepared fortified positions. [138]\r\n\r\nTerritories under the control of the warring parties at the end of April 1913 and the Midia-Enos line defined by the peace treaty for the new Ottoman border[139]\r\nOn March 11-13, 1913, the Bulgarian-Serbian troops stormed and took the Edirne Fortress. Commandant Shukri Pasha surrenders in captivity with his 60,000th army. [140] At the same time as the invasion of Edirne, the 1st and 3th Bulgarian Army marched against Chatalja and repelled the Turks from the territories seized in January, back to their fortified position. [141] On March 31, the warring parties concluded an armistice that entered into force from the next day, April 1. [142]",
                 'to': 'en'}]}]
