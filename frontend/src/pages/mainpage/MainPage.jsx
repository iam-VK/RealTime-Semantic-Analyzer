import './MainPage.css'
import Header from "../../components/header/Header"
import Body from "../../components/body/Body"
import SideBar from "../../components/sidebar/SideBar"

function MainPage()
{
    return (
        <div>
            <div className="sidebar">
                <SideBar />
            </div>
            <div className="appcontent">
                <Header subtitle={"Emotion Analysis"} />
                <Body path={"classify-emotion/"} />
            </div>
        </div>
    )
}

export default MainPage
