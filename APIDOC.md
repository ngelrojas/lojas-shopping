#### Description API

##### User API methods

-   Method POST: /auth
-   Description:
    -- method login user, using jwt token

-   Method POST: /user
-   Description:
    -- method register/create a new user, this method send and email to confirmation resgister.
    -- a complemente this method there is and method ACTIVATE

-   Method PUT: /activate/{uid}/{token}
-   Description:
    -- method update status activate through the email user sent

-   Method GET: /user/{id}
-   Description:
    -- method retrieve about personal information the current user logged in

-   Method PUT: /user/{id}
-   Description:
    -- method update about personal information the current user logged in

-   Method DELETE: /user/{id}
-   Description:
    -- method do soft-delete, instead to the hard-delete, use an status `is_delete=True`

##### Profile API methods

there are two profiles, one is `profile buyer` and the `profile seller`

when user is created by default have a `profile buyer`

user can have two profiles or one.

-   Method GET: /profile-buyer/{id}
-   Description:
    -- method retrieve about information profile buyer the current user logged in

-   Method PUT: /profile-buyer/{id}
-   Descirption:
    -- method updated about information profile buyer the current user logged in

-   Method POST: /profile-seller
-   Description:
    -- method create profile seller the current user logged in

-   Method GET: /profile-seller/{id}
-   Description:
    -- method retrieve about information profile seller the current user logged in

-   Method PUT: /profile-seller/{id}
-   Description:
    -- method update about information profile seller the current user logged in

##### Product API methods

-   Method GET: /product
-   Description:
    -- method get a list all products the current user logged in

-   Method POST: /product
-   Description:
    -- method create a new product the current user logged in

-   Method GET: /product/{id}
-   Description:
    -- method retrieve information about the product the current user logged in

-   Method PUT: /product/{id}
-   Description:
    -- method update information about the product the current user logged in

-   Method DELETE: /product/{id}
-   Description:
    -- method do soft-delete, instead to the hard-delete user status `enable=False`

##### Order API methods

-   Method GET: /order
-   Description:
    -- get all list order the current user logged in

-   Method POST: /order
-   Description:
    -- create a order the current user logged in, inside the order have a meny product

-Method GET:/order/{id}

-   Description:
    -- method retrieve information about the order

-   Method PUT: /order/{id}
-   Description:
    -- method update information about the order

-   Method DELETE: /order/{id}
-   Description:
    -- method do soft-delete, instead to the hard-delete the current user logged in.

##### Re-activate user

Method RE-SEND-EMAIL send an email to user not received

-   Method POST /re-send-email
-   Description:
    -- method send an email to user confirmation a register

when user click in the link in your email, there are two parameters to pass the method called RE-ACTIVATE

-   Method PUT: /re-activate

-   Decription:
    -- method activate a user, using UID and TOKEN

##### recovery password

-   Method POST: /recovery-password
-   Descrition:
    -- method send email to user

-   Method PUT: /recovery-confirm
-   Description:
    -- method change/update password

all description of the each field is on [API DOC BRASILPREV ](http://3.87.243.115:1337/api/v1/brasilprev/)
