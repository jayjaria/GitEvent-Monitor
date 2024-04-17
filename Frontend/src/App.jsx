import { useEffect, useState } from 'react'
import DateConverter from "./components";
const URL = "http://127.0.0.1:5000/webhook/get_all_messages"
function App() {

  const [webhookMessages, setWebhookMessages] = useState([])
  useEffect(() => {

    function getResponse(){
      fetch(URL).then(res => res.json()).then(res => setWebhookMessages(res)).catch((err)=>console.log(err))
    }
    
    getResponse()
    const intervalId = setInterval(() => {
      getResponse()
    }, 15000);

    return () => {
      clearInterval(intervalId);
    };
  }, []); 
  
  
  function getMsg(webhookMessages){  
    const date_time = DateConverter(webhookMessages['timestamp']);
    
    if(webhookMessages['action'] == 'PUSH'){
      // {author} pushed to {to_branch} on {timestamp}
      return `${webhookMessages['author']} pushed to ${webhookMessages['to_branch']} on ${date_time}`;
    }
    else if(webhookMessages['action'] == 'PULL'){
      // {author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}
      return `${webhookMessages['author']} submitted a pull request from ${webhookMessages['from_branch']} to ${webhookMessages['to_branch']} on ${date_time}`;
    }
    else if(webhookMessages['action'] == 'MERGE'){
      // {author} merged branch {from_branch} to {to_branch} on {timestamp}
      return `${webhookMessages['author']} merged branch ${webhookMessages['from_branch']} to ${webhookMessages['to_branch']} on ${date_time}`;
    }

    return "Invalid Message";
  }
  return (
    <>
    <table>
      <tr>
        <th>Id</th>
        <th>Message</th>
      </tr>
        {webhookMessages.map((webhookMessage,i)=>{return(
          
          <tr key={i}>
            <td>{i+1}</td>
            <td>{getMsg(webhookMessage)}</td>
          </tr>
          
    
        )})}
    </table>
    </>
  )
}

export default App
