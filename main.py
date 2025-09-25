from pyscript import display, document



def ordering_form(e):
    item1 = document.getElementById('menu1')
    item2 = document.getElementById('menu2')
    item3 = document.getElementById('menu3')
    item4 = document.getElementById('menu4')
    item5 = document.getElementById('menu5')

    document.getElementById('output').innerHTML = ""

    total = (float(item1.value) * item1.checked +
             float(item2.value) * item2.checked +
             float(item3.value) * item3.checked +
             float(item4.value) * item4.checked +
             float(item5.value) * item5.checked)


    name = document.getElementById('name').value
    address = document.getElementById('address').value
    contact = document.getElementById('contact').value

    message = f""" Order Summary:
    Name  : {name}
    Address  : {address}
    Contact Number  : {contact}
    Total Amount  : ${total}

    Thank you for your order! Your food will be delivered soon.
    """

    display(message, target="output")
