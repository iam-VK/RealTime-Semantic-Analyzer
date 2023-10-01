import LinearProgress from '@mui/joy/LinearProgress';
import "./progress_bar.css"
import { useState, useEffect } from 'react';

function API({ user_input })
{
    const URL = 'http://localhost:5000/classify/' + user_input;

    const [data, setData] = useState(new Map());
    const [keysArray, setKeys] = useState([]);
    const [valuesArray, setValues] = useState([]);

    useEffect(() =>
    {
        const fetchData = async () =>
        {
            try {
                const result = await fetch(URL);
                const json = await result.json();
                const dataMap = new Map(Object.entries(json).slice(0, 4));
                setData(dataMap);
                const keys = Array.from(dataMap.keys());
                const values = Array.from(dataMap.values());
                setKeys(keys);
                setValues(values);
            } catch (error) {
                console.error(error);
            }
        };

        fetchData();
    }, [user_input]);

    return { data, keysArray, valuesArray };
}


function ProgressBar({ inputValue })
{
    const { data, keysArray, valuesArray } = API({ user_input: inputValue });

    return (
        <>
            {inputValue && inputValue.trim() !== '' && (
                <>
                    {keysArray.map((key, index) => (
                        <div className='progress_box' key={key}>
                            <h3 className='bar'>{key}</h3>
                            <LinearProgress
                                color="primary"
                                determinate
                                size="sm"
                                value={valuesArray[index]}
                                variant="soft"
                            />
                        </div>
                    ))}
                </>
            )}
        </>
    );
}

export default ProgressBar;