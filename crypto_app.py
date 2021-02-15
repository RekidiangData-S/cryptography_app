import streamlit as st
from PIL import Image


def main():
    st.title("CRYPTOGRAPHY")

    menu = ["Reverse Cipher", "Ceasar Cipher",
            "ROT13 Algorithm", "Learn More",  "About"]
    choice = st.sidebar.selectbox('Selection Application', menu)

    ##"Reverse Cipher"#################################################################################################

    if choice == "Reverse Cipher":
        st.subheader('Reverse Cipher')

        if st.checkbox("Encryption"):
            message = st.text_area('Enter plain text message :')
            translated = ''  # cipher text is stored in this variable
            i = len(message) - 1
            if st.button("Encrypt"):
                while i >= 0:
                    translated = translated + message[i]
                    i = i - 1
                st.subheader("The cipher text is :")
                st.text(translated)
        if st.checkbox("Decryption"):
            message = st.text_area('Enter cipher text message :')
            translated = ''  # cipher text is stored in this variable
            i = len(message) - 1
            if st.button("Decrypt"):
                while i >= 0:
                    translated = translated + message[i]
                    i = i - 1
                st.subheader("The plain text is :")
                st.text(translated)
        if st.checkbox("About Reverse Cipher"):
            st.markdown("""
             + __Algorithm of Reverse Cipher__

             The algorithm of reverse cipher holds the following features :

             1. Reverse Cipher uses a pattern of reversing the string of plain text to convert 
             as cipher text.
             2. The process of encryption and decryption is same.
             3. To decrypt cipher text, the user simply needs to reverse the cipher text to get 
             the plain text.

            + __Drawback__

            It is a type of substitution cipher in which each letter in the plaintext is replaced by
            a letter some fixed number of positions down the alphabet.
        """)
            image = Image.open('images/reverse_cipher.png')
            st.image(image, use_column_width=True)
    ##"Ceasar Cipher"#################################################################################################
    if choice == "Ceasar Cipher":
        st.subheader("Ceasar Cipher")

        if st.checkbox("Encryption"):

            text = st.text_area('Enter plain text message :')
            s = st.slider("Enter Shift number :", 1, 26)

            def encrypt(string, shift):
                cipher = ''
                for char in string:
                    if char == ' ':
                        cipher = cipher + char
                    elif char.isupper():
                        cipher = cipher + \
                            chr((ord(char) + shift - 65) % 26 + 65)
                    else:
                        cipher = cipher + \
                            chr((ord(char) + shift - 97) % 26 + 97)
                return cipher

            if st.button("Encrypt"):
                cipherText = encrypt(text, s)
                st.subheader("The cipher text is :")
                st.text(cipherText)

        if st.checkbox("Decryption"):
            st.subheader("In build Coming Soon ....!!!!")

            text = st.text_area('Enter cipher text message :')
            s = st.slider("Enter Shift number for Encryption :", 1, 26)

            def decrypt(string, shift):
                pass

            if st.button("Decrypt"):
                st.subheader("In build Coming Soon ....!!!!")

                #plainText = decrypt(text, s)
                #st.subheader("The plain text is :")
                # st.text(plainText)

        if st.checkbox("About Caesar Cipher"):
            st.markdown("""
            It is a type of substitution cipher in which each letter in the plaintext is replaced by 
            a letter some fixed number of positions down the alphabet.
            """)
            st.markdown("""
                + __Algorithm of Caesar Cipher__

                The algorithm of reverse cipher holds the following features :

                1. Caesar Cipher Technique is the simple and easy method of encryption technique.
                2. It is simple type of substitution cipher.
                3. Each letter of plain text is replaced by a letter with some fixed number of positions
                down with alphabet.

                + __Hacking of Caesar Cipher Algorithm__

                The cipher text can be hacked with various possibilities. One of such possibility is Brute
                Force Technique, which involves trying every possible decryption key. This technique does 
                not demand much effort and is relatively simple for a hacker.
            """)
            image = Image.open('images/ceasar_cipher.jfif')
            st.image(image, use_column_width=True)

    ##"ROT13 Algorithm"#################################################################################################

    if choice == "ROT13 Algorithm":
        st.subheader('ROT13 Algorithm')

        rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
        # Function to translate plain text

        def rot13(text):
            return text.translate(rot13trans)

        if st.checkbox("Encryption"):
            message = st.text_area('Enter plain text message :')
            if st.button("Encrypt"):
                cipherText = rot13(message)
                st.subheader("The cipher text is :")
                st.text(cipherText)

        if st.checkbox("Decryption"):
            message = st.text_area('Enter cipher text message :')
            if st.button("Decrypt"):
                cipherText = rot13(message)
                st.subheader("The plain text is :")
                st.text(cipherText)

        if st.checkbox("About ROT13 Algorithm "):
            st.markdown("""
             + __ROT13 Algorithm__

             ROT13 cipher refers to the abbreviated form Rotate by 13 places. It is a special case
              of Caesar Cipher in which shift is always 13. Every letter is shifted by 13 places to 
              encrypt or decrypt the message.

            + __Drawback__

            The ROT13 algorithm uses 13 shifts. Therefore, it is very easy to shift the characters in the 
            reverse manner to decrypt the cipher text.
            It is not a very secure algorithm and can be broken easily with frequency analysis or by just
             trying possible 25 keys whereas ROT13 can be broken by shifting 13 places. Therefore, 
             it does not include any practical use.
        """)
            image = Image.open('images/rot.jpg')
            st.image(image, use_column_width=True)
    ##"Learn More"#################################################################################################
    if choice == "Learn More":
        st.subheader("Introduction to Cryptography")
        image = Image.open('images/crypto.jfif')
        st.image(image, use_column_width=True)

        if st.checkbox("Definition"):
            st.markdown("""
        **Cryptography** is the art of communication between two users via coded messages. 
        The science of cryptography emerged with the basic motive of providing security to 
        the confidential messages transferred from one party to another. 

        Cryptography is defined as the art and science of concealing the message to introduce
         privacy and secrecy as recognized in information security.
        """)

        if st.checkbox("Terminologies of Cryptography"):
            st.markdown("""

            1. __Plain Text :__ 
            The plain text message is the text which is readable and can be understood by all users. 
            The plain text is the message which undergoes cryptography.
            2. __Cipher Text :__
            Cipher text is the message obtained after applying cryptography on plain text.
            3. __Encryption :__
            The process of converting plain text to cipher text is called encryption. It is also called as encoding.
            4. __Decryption :__
            The process of converting cipher text to plain text is called decryption. It is also termed as decoding.

            The diagram given below shows an illustration of the complete process of cryptography :
            
        """)
            image = Image.open('images/encryption.jpg')
            st.image(image, use_column_width=True)

        if st.checkbox("Characteristics of Modern Cryptography"):
            st.markdown("""
        **The basic characteristics of modern cryptography are as follows :

        + It operates on bit sequences.
        + It uses mathematical algorithms for securing the information.
        + It requires parties interested in secure communication channel to achieve privacy.
         
        """)

        if st.checkbox("Double Strength Encryption"):
            st.markdown("""
        Double strength encryption, also called as multiple encryption, is the process of encrypting 
        an already encrypted text one or more times, either with the same or different algorithm/pattern.
        The other names for double strength encryption include cascade encryption or cascade ciphering.

        __Levels of Double Strength Encryption__

        + **First layer of encryption**

        The cipher text is generated from the original readable message using hash algorithms and symmetric
        keys. Later symmetric keys are encrypted with the help of asymmetric keys. The best illustration
        for this pattern is combining the hash digest of the cipher text into a capsule. The receiver will 
        compute the digest first and later decrypt the text in order to verify that text is not tampered 
        in between.

        + **Second layer of encryption**

        Second layer of encryption is the process of adding one more layer to cipher text with same or 
        different algorithm. Usually, a 32-bit character long symmetric password is used for the same.

        + **Third layer of encryption**
        
        In this process, the encrypted capsule is transmitted via SSL/TLS connection to the communication
        partner.

        The following diagram shows double encryption process pictorially :
         
        """)
            image = Image.open('images/strength_encryption.jpg')
            st.image(image, use_column_width=True)

            st.markdown(""" 

            + **Hybrid Cryptography** 

            Hybrid cryptography is the process of using multiple ciphers of different types together 
            by including benefits of each of the cipher. There is one common approach which is usually 
            followed to generate a random secret key for a symmetric cipher and then encrypt this key via 
            asymmetric key cryptography.

            Due to this pattern, the original message itself is encrypted using the symmetric cipher and 
            then using secret key. The receiver after receiving the message decrypts the message using 
            secret key first, using his/her own private key and then uses the specified key to decrypt the 
            message.
            """)

    ##"About"#################################################################################################
    if choice == "About":
        st.write(
            'https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm')


if __name__ == "__main__":
    main()
