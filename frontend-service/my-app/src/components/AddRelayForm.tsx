import "../styles/form.css"
import { useState, useEffect } from "react";

const AddRelayForm = () => {

    const ids = [4, 17, 22, 27]

    const [name, setName] = useState('');

    const [clicked, setClicked] = useState(false)

    const handleClick = () => {
        setClicked(!clicked);
        console.log(clicked)
    }

    useEffect(() => {
        fetch(`http://10.159.66.155:5000/relay/add`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: ids[0],
                state: name
            })
        })
    }, [clicked]);

    return (

        <div className="add-relay-form">
            <h1>Add New Appliance</h1>
            <form action="">
                <label>Appliance name: </label>
                <input
                    type="text"
                    required
                    value={name} // need to trigger the setName function
                    onChange={(event) => setName(event.target.value)}
                />
            </form>
            <button onClick={handleClick}>Add Relay</button>
        </div>

    );

}

export default AddRelayForm


// <p>{ name }</p>