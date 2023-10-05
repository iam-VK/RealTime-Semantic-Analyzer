import LinearProgress from '@mui/joy/LinearProgress';
import Typography from '@mui/joy/Typography';
import "./progress_bar.css"
import { useState, useEffect } from 'react';

function API(user_input, path)
{
    const URL = 'http://localhost:5000/' + path + user_input;

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
    }, [user_input],[path]);

    return { data, keysArray, valuesArray };
}


function ProgressBar({ inputValue, path })
{
    const { data, keysArray, valuesArray } = API(inputValue,path);

    valuesArray.map((key, index) =>
    (
        key == 0 ? keysArray.splice(index, 1) && valuesArray.splice(index, 1) : null
    )
    );

    return (
        <>
            {inputValue && inputValue.trim() !== '' && (
                <div className='box'>
                    {keysArray.map((key, index) => (
                        <div className='progress_box' key={key}>
                            <h3 className='bar'>{key}</h3>
                            <LinearProgress
                                color="primary"
                                determinate
                                size="lg"
                                value={valuesArray[index]}
                                thickness={20}
                                variant="soft"
                                sx={{
                                    backgroundColor: '#121212'
                                }}>

                                <Typography
                                    level="body"
                                    fontWeight="bold"
                                    textColor="common"
                                    sx={{
                                        mixBlendMode: 'difference',
                                        fontSize: "15px"
                                    }}
                                >
                                    {valuesArray[index]} %
                                </Typography>

                            </LinearProgress>
                        </div>
                    ))}
                </div>
            )}
        </>
    );
}

export default ProgressBar;