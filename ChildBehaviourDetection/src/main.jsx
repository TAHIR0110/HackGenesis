import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { AppProvider } from './context'
import { Auth0Provider } from "@auth0/auth0-react";

ReactDOM.createRoot(document.getElementById('root')).render(
  <Auth0Provider
    domain="dev-xdyux4pbaxmtu38w.us.auth0.com"
    clientId="HJ9byfwcZRm0tXvunJNcAa5btPaeVihA"
    authorizationParams={{
      redirect_uri: window.location.origin
    }}
  >
  <AppProvider>
    <App />
  </AppProvider>
  </Auth0Provider>
);

// export 