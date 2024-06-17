import constants

import net.minecraft.item.Item as Item
import net.minecraft.item.BlockItem as BlockItem
import net.minecraft.block.Block as Block
import net.minecraft.block.material.Material as Material
import net.minecraft.block.AbstractBlock.Properties as AbstractBlockProperties
import net.minecraft.item.Item.Properties as ItemProperties
import net.minecraftforge.common.ToolType as ToolType
import net.minecraft.item.ItemGroup as ItemGroup
import net.minecraftforge.registries.ForgeRegistries as ForgeRegistries
import net.minecraftforge.registries.DeferredRegister as DeferredRegister


class ModItems:
    """
    Resource Files:
     - resources.assets.pymod.lang.en_us.json - name
     - resources.assets.pymod.models.item.snake.json - item spec
     - resources.assets.pymod.textures.item.snake.png - image
    """
    ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, constants.MOD_ID)
    SNAKE = ITEMS.register(
        "snake",
        lambda: Item(ItemProperties().tab(ItemGroup.TAB_MATERIALS))
    )

    @classmethod
    def register(cls, eventBus):
        cls.ITEMS.register(eventBus)


class ModBlocks:
    BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, constants.MOD_ID)

    SNAKE_COIL = BLOCKS.register(
        "snake_coil",
         lambda: Block(
             AbstractBlockProperties.of(Material.STONE)
             .harvestLevel(2)
             .harvestTool(ToolType.PICKAXE)
             .requiresCorrectToolForDrops()
         )
    )

    @classmethod
    def register(cls, eventBus):
        ModItems.ITEMS.register(
            "snake_coil",
            lambda: BlockItem(
                ModBlocks.SNAKE_COIL.get(),
                ItemProperties().tab(ItemGroup.TAB_MATERIALS)
            )
        )
        cls.BLOCKS.register(eventBus)
