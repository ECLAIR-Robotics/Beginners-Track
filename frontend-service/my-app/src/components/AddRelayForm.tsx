import "../styles/form.css"
import { useState } from "react";

const AddRelayForm = () => {

    const [name, setName] = useState('');

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
            <button>Add Relay</button>
            
        </div>

    );

}

export default AddRelayForm


// <p>{ name }</p>