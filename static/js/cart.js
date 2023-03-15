document.addEventListener('DOMContentLoaded', () => {
    function updateUserOrder(productId, action){
        console.log("user is logged in, sending data..")
        var url = '/update_item'

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action
            })
        })
        .then ((response) => {
            return response.json()
        })
        .then ((data) => {
            console.log('data: ',data)
            location.reload()
        })
    }

    const addToCartButtons = document.getElementsByClassName("update-cart")
    console.log(addToCartButtons.length)

    for (let index = 0; index < addToCartButtons.length; index++) {
        const button = addToCartButtons[index]
        button.addEventListener('click', () => {
            var productoId = button.dataset.producto
            var action = button.dataset.action
            console.log(productoId, action)

            console.log('user', user)

            if (user == 'AnonymousUser') {
                console.log("User is not authenticated")
            }
            else {
                updateUserOrder(productoId, action)
            }
        })
    }
})