import './SC_Page.css'
import Header from "../../components/header/Header"
import Body from "../../components/body/Body"
import SideBar from "../../components/sidebar/SideBar"

function SC_Page()
{
    return (
        <div>
            <div className="sidebar">
                <SideBar />
            </div>
            <div className="appcontent">
                <Header subtitle={"Sentence Analysis"}/>
                <Body path={"classify-sentence/"} />
            </div>
        </div>
    )
}

export default SC_Page
