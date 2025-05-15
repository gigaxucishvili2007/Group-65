"""პაროლი,
,
მომხმარებელი შეიყვანს პაროლს. თუ პაროლი 8-ზე ნაკლები სიმბოლოა — დაბეჭდე "პაროლი ძალიან მოკლეა", 
თუ 8 ან მეტი — "პაროლი მიღებულია"."""

password = input("Ente your password :")
if len(password) < 8:
    print("Password is very short")
elif len(password) == 8 or len(password) > 8:
    print("Password is Accepted")