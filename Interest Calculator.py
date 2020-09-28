print ('    █ █▄░█ ▀█▀ █▀▀ █▀█ █▀▀ █▀ ▀█▀')
print ('    █ █░▀█ ░█░ ██▄ █▀▄ ██▄ ▄█ ░█░')
print ('               ')
print ('    █▀▀ ▄▀█ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█')
print ('    █▄▄ █▀█ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄')
print ('     Tᴏᴏʟ Oᴡɴᴇʀ: PʀᴏTᴇᴄʜ2206')
print ('     Sᴄʀɪᴘᴛ ᴍᴀᴅᴇ ʙʏ: Sɪᴀ')
print ('     Eᴅɪᴛᴇᴅ ʙʏ: AᴍᴀᴛᴜᴇʀCᴏᴅᴇʀ')
print ('     YᴏᴜTᴜʙᴇ: AᴍᴀᴛᴜᴇʀCᴏᴅᴇʀ PʀᴏTᴇᴄʜ')
print ('<<||_________________________________________||>>')
#calculation of Simple Interest and Compound Interest.
p=float(input("Enter the Principal amount:"))
r=float(input("Enter the Rate of interest:"))
t=float(input("Enter the Time period:"))
#calculating the Simple Interest;
si=r/100*p*t
#calculating the amount;
a=p+si
print("Simple Interest:",si)
print("Amount at the end of time period:",a)
#calculating the Compound Interest;
#calculating the amount;
am=p*(1+r/100)**t
#calculating Compound Interest;
ci=am-p
print("Compound Interest:",ci)
print("Amuont at the end of the Time period:",am)