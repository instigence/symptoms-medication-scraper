fetch('https://www.drugs.com/cg/malaria.html') 
symptoms= response.css('.contentBox h2:contains("signs and symptoms")~ul')[0].get().replace("<ul>", "").replace("<li>", "").replace("</ul>", "").replace("</li>", "").split("\n") 
symptoms = list(filter(lambda sym: sym != '', symptoms)) 
print(symptoms)