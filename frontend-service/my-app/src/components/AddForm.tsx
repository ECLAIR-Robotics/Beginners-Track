import { ARButton } from './ARButton';
import { useState } from 'react';
import { ControlButton2 } from './ControlButton2';

export default function AddForm() {

    const [relayname, setRelayName] = useState('');

    const [buttons, setButtons] = useState([]);

    const addRelay = (e: React.MouseEvent) => {
        e.preventDefault();
        if (relayname !== '') {
            console.log('Relay Name: ' + relayname);
            setButtons([...buttons, relayname]);
            setRelayName('');
        }
    };

    const runControlButton = ({ currentTarget: { value } }) => {
        console.log(`${value} clicked`);

    };

    return (
        <form>
            <div className="space-y-6">

                <h2 className="text-base font-semibold leading-7 text-gray-900">
                    Add New Appliance
                </h2>

                <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                    <div className="sm:col-span-4">

                        <label htmlFor="relayname" className="block text-sm font-medium leading-6 text-gray-900">
                            Relay Name:
                        </label>

                        <div className="mt-2">
                            <div className="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">

                                <input
                                    type="text"
                                    className="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
                                    placeholder="Type Here"
                                    value={relayname}
                                    onChange={e => setRelayName(e.target.value)}
                                />
                            </div>
                        </div>

                    </div>
                </div>

                <ARButton onClick={addRelay}>Add Relay</ARButton>
                {
                    buttons.map((button) => (
                        <ControlButton2 type="button" key={button} value={button} onClick={runControlButton}>
                            {button}
                        </ControlButton2>
                    ))
                }


            </div>
        </form>
    )
}
