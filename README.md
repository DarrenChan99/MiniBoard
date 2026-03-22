# MiniBoard
A 3x3 macro pad with OLED display. 
One idea to use this layout is to keep track of daily habits and track them to promote better productivity.

<h2> Key Mapping </h2>

<ul>
<li>[1-6]: Up to 6 individual habits that can be mapped</li>
<li>[7 + 8]: Used to navigate across the individual habits and the consistancy overtime </li>
<li>[9]: Reset the board</li>
</ul>

<h2>Why?</h2>
<ol>
 <li>I wanted to learn electronics and pcb design</li>
 <li>Create a real world design that is functional</li>
 <li>Explore new enviroments like KiCad and Fusion 360</li>
</ol>

<h1> CAD </h1>
<img width="634" height="685" alt="Screenshot 2026-03-20 at 11 16 19 PM" src="https://github.com/user-attachments/assets/36ef13b6-aecb-4bf6-9be7-3b6d578a00e5" />

<h1> PCB </h1>
<p>Made with KiCad</p>

<p> Schematic </p>
<img width="963" height="460" alt="Screenshot 2026-03-20 at 11 18 28 PM" src="https://github.com/user-attachments/assets/8ae56274-80ac-4746-8ef1-8b4d1d5d330f" />

<p> PCB </p>
<img width="524" height="642" alt="Screenshot 2026-03-20 at 11 17 46 PM" src="https://github.com/user-attachments/assets/0dc0219e-4e2e-45ec-86f0-10739ec2348d" />

<h1> Firmware </h1>
<p> This macropad used <a href="https://github.com/KMKfw/kmk_firmware">KMK</a> firmware with CircuitPython. </p>
<ul> 
 <li>Used to implment button mapping</li>
 <li>Displaying and refreashing OLED</li>
</ul>
<h1> BOM </h1>
<table>
    <thead>
        <tr>
            <th>Component</th>
            <th>Quantity</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Seeed Studio XIAO RP2040</td>
            <td>1</td>
            <td>Microcontroller board</td>
        </tr>
        <tr>
            <td>Cherry MX Switches</td>
            <td>9</td>
            <td>Mechanical key switches</td>
        </tr>
        <tr>
            <td>DSA Keycaps</td>
            <td>9</td>
            <td>Blank Keycaps</td>
        </tr>
        <tr>
            <td>0.91" OLED Display</td>
            <td>1</td>
            <td>4 pin I2C display</td>
        </tr>
        <tr>
            <td>1N4148 Diodes</td>
            <td>6</td>
            <td>Through-hole signal diodes</td>
        </tr>
        <tr>
            <td>M3x5x4 Heatset Inserts</td>
            <td>4</td>
            <td>Threaded inserts for case assembly</td>
        </tr>
        <tr>
            <td>M3x16mm Screws</td>
            <td>4</td>
            <td>Mounting case</td>
        </tr>
        <tr>
            <td>3D Printed Case</td>
            <td>1</td>
            <td>2-part custom enclosure</td>
        </tr>
        <tr>
            <td>Soldering Iron</td>
            <td>1</td>
            <td>Assembly tool</td>
        </tr>
    </tbody>
</table>






