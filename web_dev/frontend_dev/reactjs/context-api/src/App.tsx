import Navbar from "./components/Navbar"
import Settings from "./components/Settings"
import ThemeProvider from "./context/theme-context"

const App = () => {
  return (
    <ThemeProvider>
      <Navbar />
      <Settings />
    </ThemeProvider>
  )
}

export default App
