import { useTheme } from "../hooks/use-theme";

const Navbar = () => {
    const { theme } = useTheme();

  return (
    <div>
      <h2>Navbar</h2>
      <h3>Current Theme: {theme} </h3>
    </div>
  )
}

export default Navbar
