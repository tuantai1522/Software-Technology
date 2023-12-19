const addToCart = (id, name, price) => {
    fetch("/api/add-to-cart", {
        method: 'post',
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            'Content-Type': 'application/json'
        }

    })
        .then(res => res.json())
        .then(data => {
            let counter_cart = document.getElementById('counter-cart');
            counter_cart.textContent = data.total_quantity;
        } )
        .catch(err => console.log(err))
}

const pay = () => {
    console.log("Me");
    if (confirm("Bạn có chắc muốn thanh toán không ?")) {
        fetch("/api/pay", {
            method: 'post',

        })
            .then(res => res.json())
            .then(data => {
                if(data.code == 200)
                    location.reload();
            })
            .catch(err => console.log(err))
    }
}