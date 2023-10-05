import "./header.css"
function Header({ subtitle })
{
    return (
        <>
            <header className="header">
                <h1>Real-Time Semantic Analysis</h1>
            </header>
            <div class="container">
                <div class="typed-out">
                    {subtitle}
                </div>
            </div>
        </>
    )
}


export default Header