# QuantumJam
<h4> This repo hosts the files to a small game we called 'Shape Attack' made for a game jam focused on Quantum Mechanics with its theme as 'patterns'. </h4>

<div>
  <h2>The Development Process</h2>
  <ul>
    <h3>Planning</h3>
    <ul>
      <li>
        My partner <a href="https://github.com/the20thtry">Derek</a> and I begun this project by brainstorming a simple idea irrespecitve of quantum mechanics 
        (since we weren't familiar with them). With the intention of implementing them thematically once we had establish a foundation for the game. 
        For this project we decided to use python paired with the pygame library. <a href="https://github.com/M-i-K-e-G">Mike</a> assisted in creating 
        graphical assets for the project. 
      </li>
    </ul>
    <h3>Workload</h3>
    <ul>
      <li>
        Before starting we familiarized ourselves with pygame as we had never used it before. Afterwards to start we split the workload
        into two chunks, I was assigned enemy related systems while Derek worked on player systems, along the way we discussed various problems
        that we ran into together to solve using different perspectives and understand new concepts better.
      </li>
      <li>
        There were moments when one of us would finish our tasks and be unable to continue until the counterpart system was finished or at least
        updated to be comptabale. To maintain our efficient workflow and keep pace we circumvented this by taking on seperate mechanics or systems
        that were indepent of those currenlty being waited on. 
      </li>
    </ul>
    <h3><a href="https://github.com/Alex-z01/QuantumJam/blob/main/player.py">Player Class</a></h3>
    <ul>
      <li>
        The player class only takes in a path as an arg, this path must point to an image. It initialized a culmniation
        of variables relating to the player's transform and game information such as health and speed. The player class originally did not inherit
        from pygame.sprite.Sprite so it handled input via a function that was called every frame from main, after the sprite pygame refactor I created
        a function called 'actions' which would be called every tick/frame within the player object's update method.
      </li>
      <li>
        The player class also had a weapon switch mechanic, take damage method used to respond to collisions from enemies, and an attack mechanic
        which would respond differently based on the current weapon value. 
      </li>
      <li>
        To handle collisions from the player's weapon we implemented a projectile sprite group local to the player, on attack input a projectile object
        would be instantiated which would have its own set of methods for collisions which would be called from the player's pygame update method.
      </li>
    </ul>   
    <h3><a href="https://github.com/Alex-z01/QuantumJam/blob/main/enemy.py">Enemy Class</a></h3>
    <ul>
      <li>
        This class is fundamentally similar to the player, aside from the addition of a target follow mechanic and a few more constructor parameters. 
      </li>
    </ul>
    <h3><a href="https://github.com/Alex-z01/QuantumJam/blob/main/enemyspawner.py">Spawner</a></h3>
    <ul>
      <li>
        The spawner class is a simple class that allows for the rapid and easy creation of any enemy object <i>n</i> number of times.
      </li>
    </ul>
    <h3>
      <a href="https://github.com/Alex-z01/QuantumJam/blob/main/particle.py">Particle Projectile</a>
      <br>
      <a href="https://github.com/Alex-z01/QuantumJam/blob/main/waveProj.py">Wave Projectile</a>
    </h3>
  </ul> 
</div>  

<h2>Shape Attack</h2>
<p> 2D Arcade shooter with simple yet portable and scalable player and enemy implementations </p>
